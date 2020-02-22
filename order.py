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
            username = dictionary["username"]
            type = dictionary["type"]
            destination = dictionary["destination"]

            sqlConnection = connectToSQLDB()
            cursor = sqlConnection.cursor()
            cursor.execute(f"SELECT custid FROM customers WHERE username = {username}")
            custid = cursor.fetchall()
            cursor.execute(f"INSERT INTO orders (custid, type, destination) VALUES "
                           f"({custid}, {type}, {destination})")
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
        print("got")
        self.send_response(200)
        self.end_headers()
        self.wfile.write("response body \r\n")
