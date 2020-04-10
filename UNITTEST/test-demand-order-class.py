import unittest
import sys
from test.test_copy import order_comparisons
sys.path.insert(1, '../')
from customers import Customer

class TestDemandCustomerClass(unittest.TestCase):

    # Write your test cases here
    def testCreateOrder(self):
        order = Order(123,321, ServiceType.DRYCLEANING,'destination?',2018-03-29T13:34:00.000)
        
        self.assertEqual(123, order.orderid)
        self.assertEqual(321, order.custid)
        self.assertEqual(ServiceType.DRYCLEANING, order.serviceType)
        self.assertEqual('destination?', order.destination)
        self.assertEqual(2018-03-29T13:34:00.000, order.timeOrderMade)
        
        print(order)
        print()     
        
if __name__ == '__main__':
    unittest.main()