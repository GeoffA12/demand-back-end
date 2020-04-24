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

    # Test 401 status response on POST request for login.py when the username isn't stored in our database
    def test_login_post_status_incorrect_username(self):
        url = "https://demand.team22.softwareengineeringii.com/loginHandler"

        payload = "{\"username\" : \"Notinthedatabase\", \"password\" : \"HAHA\"}"
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data = payload)
        statusCode = response.status_code
        self.assertEqual(statusCode, 401)
    
    # Test 401 status on POST request for login.py when the password isn't stored in our database
    def test_login_post_status_incorrect_password(self):
        url = "https://demand.team22.softwareengineeringii.com/loginHandler"

        payload = "{\"username\" : \"Geoff\", \"password\" : \"LOLPASSWORD\"}"
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data = payload)
        statusCode = response.status_code
        self.assertEqual(statusCode, 401)

    # Test 401 status on POST request for login.py when the password and username aren't stored in our database
    def test_login_post_status_incorrect_password_incorrect_username(self):
        url = "https://demand.team22.softwareengineeringii.com/loginHandler"

        payload = "{\"username\" : \"randomuser\", \"password\" : \"randompassword\"}"
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data = payload)
        statusCode = response.status_code
        self.assertEqual(statusCode, 401)

    def test_successful_login_1(self):
        url = "https://demand.team22.softwareengineeringii.com/loginHandler"

        payload = "{\"username\" : \"Geoff\", \"password\" : \"HAHA\"}"
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data = payload)
        statusCode = response.status_code
        self.assertEqual(statusCode, 200)

    
    def test_successful_login_1(self):
        url = "https://demand.team22.softwareengineeringii.com/loginHandler"

        payload = "{\"username\" : \"Michaels\", \"password\" : \"password\"}"
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data = payload)
        statusCode = response.status_code
        self.assertEqual(statusCode, 200)
    


if __name__ == '__main__':
    unittest.main()


