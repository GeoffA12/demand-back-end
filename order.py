
# Python demand order class. 
class Order():

    # Class constructor. Set instance variables below. 
    # Each order instance will have a customer id, service type, and destination.
    def __init__(self, orderid, custid, sType, destination, timeOrderMade):
        self.__orderid = orderid
        self.__custid = custid
        self.__sType = sType
        self.__destination = destination
        self.__timeOrderMade = timeOrderMade
        
        
    #Defining our getter methods
    # This method might be a bit tricky due to the fact that we'll need to retrieve a piece of data 
    # identifying the user who made the order from the front end (using session storage, might need to change up a little of 
    # back end for this 
    # but not sure yet).
    def getOrderIdOfOrder(self):
        resturn self.__orderid
        
        
    def getCustomerIdOfOrder(self):
        return self.__custid

    
    def getOrderType(self):
        return self.__sType

    
    def getDestinationAddress(self):
        return self.__destination
        
        
    def getTimeOrderMade(self):
        return self.__timeOrderMade

    
    # toString() method
    def __str__(self):
        return "Order ID: " + self.getOrderIdOfOrder + " Customer ID: "+ + self.getCustomerIdOfOrder() + " Order Type: " + self.getOrderType() + " Destination: " + self.getDestinationAddress() + " Order Made: " + self.getTimeOrderMade
        
    def getOrderInfo(self):
        return self.__str__