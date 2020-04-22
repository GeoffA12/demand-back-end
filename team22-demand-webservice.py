import http.server
from http.server import BaseHTTPRequestHandler
import json
import utils.databaseutils as databaseutils
import requests
from enums.servicetype import ServiceType


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    ver = '0.1.2'

    # how to convert the body from a string to a dictionary
    # use 'loads' to convert from byte/string to a dictionary!
    def getPOSTBody(self):
        length = int(self.headers['content-length'])
        body = self.rfile.read(length)
        return json.loads(body)

    def do_POST(self):
        status = 404
        path = self.path
        print(path)
        responseDict = {'Success': False}

        if '/demand/order/req' in path:
            status = 400
            dictionary = self.getPOSTBody()
            # to access a specific key from the dictionary:
            print(dictionary)
            username = dictionary['username']
            serviceType = dictionary['serviceType']
            serviceType = ServiceType.translate(serviceType)
            destination = dictionary['destination']
            timeOrderMade = dictionary['timeOrderMade'][:-5]

            print(username)
            print(serviceType)
            print(destination)
            print(timeOrderMade)

            # sqlConnection = databaseutils.connectToSQLDB()
            # cursor = sqlConnection.cursor()
            # cursor.execute('SELECT custid FROM customers WHERE username = %s OR email = %s', (username,username))
            # custid = cursor.fetchone()
            custid = databaseutils.getCustomerIDByCredentials(username)
            print(custid)
            if custid is not None:
                custid = custid[0]
                humanReadable = destination.pop('humanReadable')
                print(custid)
                # cursor.execute('INSERT INTO orders VALUES (Null, %s, %s, %s, %s)',
                #                (custid, serviceType.lower(), humanReadable, timeOrderMade))
                # sqlConnection.commit()
                # cursor.execute('SELECT orderid FROM orders WHERE custid = %s AND date_ordered = %s', (custid,timeOrderMade))
                # orderid = cursor.fetchone()[0]
                orderData = (custid, serviceType.lower(), humanReadable, timeOrderMade,)
                databaseutils.storeOrder(orderData)

                data = (custid, timeOrderMade,)
                orderid = databaseutils.getOrderID(data)

                print(orderid)
                custid = int(custid)
                orderid = int(orderid)

                lat, lon = destination['lat'], destination['lon']

                # rebuild post body dictionary
                orderDict = {
                    'serviceType': serviceType,
                    'custid': custid,
                    'orderid': orderid,
                    'destination': {
                        'lat': lat,  # must always be between -90 and 90
                        'lon': lon
                    },
                    'timeOrderMade': timeOrderMade
                }

                # Make API call to vehicleRequest, POSTing our order dictionary. Our API will need partial order
                # dictionary information.
                print(orderDict)
                orderDict = json.dumps(orderDict)
                response = requests.post('https://supply.team22.softwareengineeringii.com/supply/vehicles/req',
                        orderDict)
                status = response.status_code
                if status == 200:
                    responseDict['Vehicle Info'] = response.json()

        self.send_response(status)
        self.end_headers()
        res = json.dumps(responseDict)
        bytesStr = res.encode('utf-8')
        self.wfile.write(bytesStr)


def main():
    # Define the port your server will run on:
    # Using 4001 as an example! Yours may run on another port!
    # Consult with Devops Coordinator to find out which port
    # your server should be running on!
    port = 4004
    # Create an http server using the class and port you defined
    httpServer = http.server.HTTPServer(('', port), SimpleHTTPRequestHandler)
    print("Running on port", port)
    # this next call is blocking! So consult with Devops Coordinator for
    # instructions on how to run without blocking other commands frombeing
    # executed in your terminal!
    httpServer.serve_forever()


if __name__ == "__main__":
    main()
