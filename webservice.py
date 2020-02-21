import http.server
from http.server import BaseHTTPRequestHandler
import json
import urllib.parse
import mysql.connector as mariadb
import requests

def connectToMariaDB():
    return mariadb.connect(user='root', password='ShinyNatu34', database='team22demand')

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

        # If we are receiving a request to register an account
        if "/registerHandler" in path:
            dictionary = self.getPOSTBody()
            # To access a specific key from the dictionary:
            print(dictionary)
            username = dictionary['username']
            password = dictionary['password']
            email = dictionary['email']
            phone = dictionary['phoneNumber']

            mariadb_connection = connectToMariaDB()
            cursor = mariadb_connection.cursor()
            cursor.execute("SELECT username FROM customers")
            rows = cursor.fetchall()
            usernames = [x[0] for x in rows]

            userAlreadyExists = False
            for x in usernames:
                if x == username:
                    userAlreadyExists = True
            status = None
            if userAlreadyExists:
                status = 401
            else:
                status = 200
                newCursor = mariadb_connection.cursor()
                print(username)
                print(password)
                newCursor.execute("INSERT INTO customers (username, password, email, phone) VALUES (%s, %s, %s, %s)",
                                  (username, password, email, phone))
                mariadb_connection.commit()
            print(status)
            responseDict['Success'] = True

        # If we are receiving a request for a client to long into the website
        elif "/loginHandler" in path:
            dictionary = self.getPOSTBody()
            # To access a specific key from the dictionary:
            print(dictionary)
            username = dictionary['username']
            password = dictionary['password']

            mariadb_connection = connectToMariaDB()
            cursor = mariadb_connection.cursor()
            cursor.execute("SELECT username, password FROM customers")
            rows = cursor.fetchall()
            username_list = [x[0] for x in rows]
            password_list = [x[1] for x in rows]

            # check all usernames and passwords in the table to make sure we're keeping our usernames unique
            userAlreadyExists = False
            for (x, y) in zip(username_list, password_list):
                print(x)
                print(y)
                if x == username and y == password:
                    userAlreadyExists = True
                    break
            status = None
            # We'll send a 401 code back to the client if the user hasn't registered in our database
            if userAlreadyExists:
                status = 200
            else:
                status = 401
            print(status)
            responseDict['Success'] = True


        elif '/orderHandler' in path:
            dictionary = self.getPOSTBody()
            print(dictionary)

            mariadb_connection = connectToMariaDB()
            cursor = mariadb_connection.cursor()
            cursor.execute("INSERT INTO orders") # Need to solidify order table
            mariadb_connection.commit()

            # Make API call to vehicleRequest, POSTing our order dictionary. Our API will need partial order
            # dictionary information.
            response = requests.post("https://supply.team22.softwareengineeringii.com/api/cs/vehicleRequest", dictionary)
            status = response.status_code
            responseDict['Status'] = status
            if 200 <= status < 300:
                responseDict['Vehicle Info'] = response.json()

        else:
            status = 404

        self.send_response(status)
        self.end_headers()
        res = json.dumps(responseDict)
        bytesStr = res.encode('utf-8')
        self.wfile.write(bytesStr)



    def do_GET(self):
        print('do stuff')

    def do_UPDATE(self):
        print('do stuff')

    def do_OPTIONS(self):
        print('do stuff')

def main():
    # Define the port your server will run on:
    # Using 4001 as an example! Yours may run on another port!
    # Consult with Devops Coordinator to find out which port
    # your server should be running on!
    port = 4002
    # Create an http server using the class and port you defined
    httpServer = http.server.HTTPServer(('', port), SimpleHTTPRequestHandler)
    print("Running on port", port)
    # this next call is blocking! So consult with Devops Coordinator for
    # instructions on how to run without blocking other commands frombeing
    # executed in your terminal!
    httpServer.serve_forever()

if __name__ == "__main__":
    main()