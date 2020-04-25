import unittest
import sys
#from test.test_copy import order_comparisons
sys.path.insert(1, '../')
from order import Order
from enums.servicetype import ServiceType

class TestDemandCustomerClass(unittest.TestCase):

    def testCreateOrder(self):
        order = Order(1234, 321, ServiceType.DRYCLEANING, "520 Woodward St.", "2018-03-29T13:34:00.000")
        
        self.assertEqual(321, order._orderid)
        self.assertEqual(1234, order._custid)
        self.assertEqual(ServiceType.DRYCLEANING, order.serviceType)
        self.assertEqual("520 Woodward St.", order.destination) #how to show destination via lats and longs? HUMANREADABLE
        self.assertNotEqual("2020-04-10T13:30:00.000", order.timeOrderMade)
        
        print(order)
        print()     
        
if __name__ == '__main__':
    unittest.main()