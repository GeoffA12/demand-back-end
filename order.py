import http.server
from http.server import BaseHTTPRequestHandler
import json
import urllib.parse
import mysql.connector as mariadb
import requests


class orderHandler(BaseHTTPRequestHandler):
    ver = '0.0'
    dir = '/home/team22/'
    def do_POST(self):
        path = self.path
        print(path)


        responseDict = {}
        responseDict['Status'] = 405
        responseDict['Vehicle Info'] = None

        if path == f'{dir}orderHandler':
            mariadb_connection = mariadb.connect(user='root', password='ShinyNatu34', database='team22demand')
            cursor = mariadb_connection.cursor()

            length = int(self.headers['content-length'])
            body = self.rfile.read(length)

            dictionary = json.loads(body)
            print(dictionary)

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

            self.send_response(status)
            self.end_headers()

        else:
            print("I got to your handler but I didn't find the correct path")
            self.send_response(405)
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
