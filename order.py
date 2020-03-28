
# Python demand order class. 
class Order():

    # Class constructor. Set instance variables below. 
    # Each order instance will have a customer id, service type, and destination.
    def __init__(self, custid, sType, destination):
        self.__custid = custid
        self.__sType = sType
        self.__destination = destination
        
        
    #Defining our getter methods
    # This method might be a bit tricky due to the fact that we'll need to retrieve a piece of data 
    # identifying the user who made the order from the front end (using session storage, might need to change up a little of 
    # back end for this 
    # but not sure yet).
    def getCustomerIdOfOrder(self):
        return self.__custid

    
    def getOrderType(self):
        return self.__sType

    
    def getDestinationAddress(self):
        return self.__destination

    
    # toString() method
    def __str__(self):
        return self.getCustomerIdOfOrder() + " " + self.getOrderType() + " " + self.getDestinationAddress()
        
    def getOrderInfo(self):
        return self.__str__