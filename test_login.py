import http.client
import requests
import unittest

class Test_Login_Py(unittest.TestCase):
    #Test 200 status response on GET request for login.py
    def test_login_get_status(self):
        url = "https://demand.team22.softwareengineeringii.com/loginHandler"

        payload  = {}
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data = payload)
        statusCode = response.status_code
        self.assertEqual(statusCode, 200)

    def test_login_post_status_incorrect_username(self):
        url = "https://demand.team22.softwareengineeringii.com/loginHandler"

        payload = "{\"username\" : \"Notinthedatabase\", \"password\" : \"HAHA\"}"
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data = payload)
        statusCode = response.status_code
        self.assertEqual(statusCode, 401)

if __name__ == '__main__':
    print("Main")
    unittest.main()


