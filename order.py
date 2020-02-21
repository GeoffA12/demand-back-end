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
        responseDict = {'Success': False, 'Vehicle Info': None}

        if '/orderHandler' in path:
            dictionary = self.getPOSTBody()
            # To access a specific key from the dictionary:
            print(dictionary)

            sqlConnection = connectToSQLDB()
            cursor = sqlConnection.cursor()
            cursor.execute("INSERT INTO orders")  # Need to solidify order table
            sqlConnection.commit()

            # Make API call to vehicleRequest, POSTing our order dictionary. Our API will need partial order
            # dictionary information.
            response = requests.post("https://supply.team22.softwareengineeringii.com/vehicleRequest", dictionary)
            status = response.status_code
            if status == 200:
                responseDict['Vehicle Info'] = response.json()

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

        if "orderHanlder" in path:
            print('do stuff')
            # Do stuff

        else:
            print("I got to your handler but I didn't find the correct path")
            # self.wfile.write(p.encode('utf-8'))
            self.send_response(405)
            self.end_headers()
