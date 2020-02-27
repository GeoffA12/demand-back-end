import http.client
import unittest
class Test_Login_Py(unittest.TestCase):
    #Test 200 status response on GET request for login.py
    def test_stats(self):
    
        conn = http.client.HTTPConnection("demand.team22.softwareengineeringii.com:4001")

        headers = {
            'cache-control': "no-cache"
        }

        conn.request("GET", "/loginHandler", headers=headers)

        res = conn.getresponse()
        data = res.status
        self.assertEqual(data, 200)

if __name__ == '__main__':
    unittest.main()


