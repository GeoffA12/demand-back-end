import unittest
import sys
sys.path.insert(1, '../')
from customers import Customer

postBody = {
    'username': username,
    'email': email,
    'password': password,
    'firstname': firstname,
    'lastname': lastname,
    'phonenumber': phonenumber
    }

class TestDemandCustomerClass(unittest.TestCase):

    # Write your test cases here
    def testCreateCustomer(self):
        cust = Customer(**postBody)
        
        self.assertEqual(username, cust.username)
        self.assertEqual(email, cust.email)
        self.assertEqual(password, cust.password)
        self.assertEqual(firstname, cust.firstname)
        self.assertEqual(lastname, cust.lastname)
        self.assertEqual(phonenumber, cust.phonenumber)
        self.assertEqual(custid, cust.custIDs)
        
        print(cust)
        print()
        
    def testCustomerUsername(self):
        cust = Customer(**postBody)
        
        self.assertEqual(username, cust.username)
        self.assertEqual(custid, cust.custIDs)
        # confusion
        
        print(cust)

if __name__ == '__main__':
    unittest.main()

