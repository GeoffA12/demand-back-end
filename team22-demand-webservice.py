import http.server
from http.server import BaseHTTPRequestHandler
import json
import urllib.parse
import mysql.connector as sqldb
import requests

def connectToSQLDB():
    return sqldb.connect(user='root', password='password', database='team22demand', port=6022)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    ver = '1.0'

    # How to convert the body from a string to a dictionary
    # use 'loads' to convert from byte/string to a dictionary!
    def getPOSTBody(self):
        length = int(self.headers['content-length'])
        body = self.rfile.read(length)
        return json.loads(body)

    def do_POST(self):
        path = self.path
        print(path)
        responseDict = {'Success': False}
        
        if '/loginHandler' in path:
            dictionary = self.getPOSTBody()
            # To access a specific key from the dictionary:
            print(dictionary)
            username = dictionary['username']
            password = dictionary['password']

            sqlConnection = connectToSQLDB()
            cursor = sqlConnection.cursor()
            cursor.execute('SELECT username, password FROM customers')
            rows = cursor.fetchall()
            usernameList = [x[0] for x in rows]
            passwordList = [x[1] for x in rows]

            # Make a dictionary from the usernameList and passwordList where the key:value pairs
            # are username:password
            userpass = dict(zip(usernameList, passwordList))

            if username in userpass and userpass[username] == password:
                status = 200

            # We'll send a 401 code back to the client if the user hasn't registered in our database
            else:
                status = 401

        # If we are receiving a request to register an account
        elif '/registerHandler' in path:
            dictionary = self.getPOSTBody()
            # To access a specific key from the dictionary:
            print(dictionary)
            username = dictionary['username']
            password = dictionary['password']
            email = dictionary['email']
            phone = dictionary['phoneNumber']

            sqlConnection = connectToSQLDB()
            cursor = sqlConnection.cursor()
            cursor.execute('SELECT username FROM customers')
            rows = cursor.fetchall()
            usernameList = [x[0] for x in rows]

            # The equivalent of arr.contains(e)
            if username in usernameList:
                status = 401
            else:
                status = 200
                newCursor = sqlConnection.cursor()
                print(username)
                print(password)
                newCursor.execute('INSERT INTO customers (username, password, email, phone) VALUES (%s, %s, %s, %s)',
                                  (username, password, email, phone))
                sqlConnection.commit()
                responseDict['Success'] = True

        elif '/orderHandler' in path:
            dictionary = self.getPOSTBody()
            # To access a specific key from the dictionary:
            print(dictionary)
            username = dictionary['username']
            sType = dictionary['serviceType']
            destination = dictionary['destination']

            '''
            add the current time to the order dictionary
            attribute will be 'timeOrderMade'
            '''

            print(username)
            print(sType)
            print(destination)

            sqlConnection = connectToSQLDB()
            cursor = sqlConnection.cursor()
            cursor.execute('SELECT custid FROM customers WHERE username = %s', (username,))
            custid = cursor.fetchone()[0]
            print(custid)
            if custid is not None:
                print(custid)
                cursor.execute('INSERT INTO orders (custid, type, destination) VALUES (%s, %s, %s)',
                               (custid, sType, destination))
                sqlConnection.commit()
                '''
                appened customer id into dictionary as well. 
                attribute will be 'customerID'
                '''
                # Make API call to vehicleRequest, POSTing our order dictionary. Our API will need partial order
                # dictionary information.
                response = requests.post('https://supply.team22.softwareengineeringii.com/vehicleRequest', dictionary)
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