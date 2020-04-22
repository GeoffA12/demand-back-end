import http.server
from http.server import BaseHTTPRequestHandler
import json
import urllib.parse
import mysql.connector as sqldb
import requests

# move to utils ?!
def connectToSQLDB():
    return sqldb.connect(user='root', password='password', database='team22demand', port=6022)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    ver = '1.0'

    # how to convert the body from a string to a dictionary
    # use 'loads' to convert from byte/string to a dictionary!
    def getPOSTBody(self):
        length = int(self.headers['content-length'])
        body = self.rfile.read(length)
        return json.loads(body)

    def do_POST(self):
        path = self.path
        print(path)
        responseDict = {'Success': False} 

        if '/demand/order/req' in path:
            dictionary = self.getPOSTBody()
            # to access a specific key from the dictionary:
            print(dictionary)
            username = dictionary['username']
            serviceType = dictionary['serviceType']
            destination = dictionary['destination']
            timeOrderMade = dictionary['timeOrderMade']

            print(username)
            print(serviceType)
            print(destination)
            print(timeOrderMade)

            sqlConnection = connectToSQLDB()
            cursor = sqlConnection.cursor()
            cursor.execute('SELECT custid FROM customers WHERE username = %s OR email = %s', (username,username))
            custid = cursor.fetchone()
            print(custid)
            if custid:
                custid = custid[0]
                humanReadable = destination.pop('humanReadable')
                print(custid)
                cursor.execute('INSERT INTO orders VALUES (Null, %s, %s, %s, %s)',
                               (custid, serviceType.lower(), humanReadable, timeOrderMade))
                sqlConnection.commit()
                cursor.execute('SELECT orderid FROM orders WHERE username = %s AND date_ordered = %s', (username,timeOrderMade))
                orderid = cursor.fetchone()[0]
                print(orderid)
                custid = int(custid)
                orderid = int(orderid)
                
                lat,long = destination['lat'], destination['long']

                # rebuild post body dictionary
                orderDict = {
                    'serviceType': serviceType,
                    'custid': custid,
                    'orderid': orderid,
                    'destination': {
                        'lat': lat, #must always be between -90 and 90
                        'long': long
                        },
                    'timeOrderMade': timeOrderMade
                    }
                # serviceType, timeOrderMade, destination (lat,long(floats)), custid(int), orderid(int)
                
                '''
                appened customer id into dictionary as well. 
                attribute will be 'customerID'
                '''
                # Make API call to vehicleRequest, POSTing our order dictionary. Our API will need partial order
                # dictionary information.
                response = requests.post('https://supply.team22.softwareengineeringii.com/supply/vehicles/req', dictionary)
                status = response.status_code
                # status = 200
                if status == 200:
                    responseDict['Vehicle Info'] = response.json()
            else:
                status = 400
        else:
            status = 404

        self.send_response(status)
        self.end_headers()
        res = json.dumps(responseDict)
        bytesStr = res.encode('utf-8')
        self.wfile.write(bytesStr)

    def do_GET(self):
        path = self.path
        print(path)
        responseDict = {'Success': False}
        if '/orderConfirmation' in path:
            orderid = 123
            PARAMS = {'oid':orderid}
            response = requests.get('https://supply.team22.softwareengineeringii.com/etaRequest', PARAMS)
            data = response.json()
            status = response.status_code
            if status == 200:
                responseDict = data
        else:
            status == 404
            
            #sqlConnection = connectToSQLDB()
            #cursor = sqlConnection.cursor()
            #cursor.execute('SELECT orderid FROM orders WHERE ')
        print('got')
        self.send_response(status)
        self.end_headers()
        res = json.dumps(responseDict)
        byteStr = res.encode('utf-8')
        self.wfile.write(byteStr)

    def do_OPTIONS(self):
        print('options')
        self.send_response(200)
        self.end_headers()

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