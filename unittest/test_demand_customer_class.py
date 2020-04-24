import unittest
import sys
sys.path.insert(1, '../')
from customer import Customer

postBody = {
    'username': 'test',
    'email': 'test@email.com',
    'password': 'password',
    'firstname': 'firstname',
    'lastname': 'lastname',
    'phonenumber': '1234567890',
    }

class TestDemandCustomerClass(unittest.TestCase):

    def testCreateCustomer(self):
        cust = Customer(**postBody)
        
        self.assertEqual('test', cust.username)
        self.assertEqual('test@email.com', cust.email)
        self.assertEqual('password', cust.password)
        self.assertEqual('firstname', cust.firstname)
        self.assertEqual('lastname', cust.lastname)
        self.assertEqual('1234567890', cust.phonenumber)
        #self.assertEqual(custid, cust.custIDs)
        
        print(cust)
        print()
        
    def testCustomerUsername(self):
        cust = Customer(**postBody)
        
        self.assertEqual('test', cust.username)
        #self.assertEqual(345, cust.custid)
        # custid tdb
        
        print(cust)

if __name__ == '__main__':
    unittest.main()