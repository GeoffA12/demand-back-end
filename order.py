
# Python Demand Order Class
class Order():

    # Class constructor. Set instance variables below. 
    # Each order instance will have an order id, customer id, service type, destination, and time order made.
    def __init__(self, custid, orderid, sType, destination, timeOrderMade):
        #self._orderid = orderid
        self._custid = custid
        self._orderid = orderid
        self._sType = sType
        self._destination = destination
        self._timeOrderMade = timeOrderMade
        
        
    # Defining our getter methods
    # this method might be a bit tricky due to the fact that we'll need to retrieve a piece of data 
    # identifying the user who made the order from the front end (using session storage, might need to change up a little of back end for this but not sure yet).
    
    #@property
    #def orderid(self):
        #return self._orderid
        
    @property
    def custid(self):
        return self._custid
    
    @property
    def orderid(self):
        return self._orderid


    @property
    def serviceType(self):
        return self._sType

    @property
    def destination(self):
        return self._destination
        
    @property
    def timeOrderMade(self):
        return self._timeOrderMade
    
    # toString() method
    def __str__(self):
        return "Customer ID: " + str(self.custid) + "Order ID: " + str(self.orderid) + " Order Type: " + str(self.serviceType) + " Destination: " + self.destination + " Order Made: " + self.timeOrderMade