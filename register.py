import http.server
from http.server import BaseHTTPRequestHandler
import json
import urllib.parse
import mysql.connector as sqldb



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

        # If we are receiving a request to register an account
        if '/registerHandler' in path:
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

            print(status)

        else:
            status = 404

        self.send_response(status)
        self.end_headers()
        res = json.dumps(responseDict)
        bytesStr = res.encode('utf-8')
        self.wfile.write(bytesStr)

    def do_GET(self):
        print('got')
        self.send_response(200)
        self.end_headers()
        self.wfile.write('response body \r\n')

    def do_OPTIONS(self):
        print('options')
        self.send_response(200)
        self.end_headers()

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
