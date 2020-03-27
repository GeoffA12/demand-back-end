
# Python demand order class. 
class Order():

    # Class constructor. Set instance variables below. 
    # def __init__(self):
        
        
    #Defining our getter methods
    # This method might be a bit tricky due to the fact that we'll need to retrieve a piece of data 
    # identifying the user who made the order from the front end (using session storage, might need to change up a little of 
    # back end for this 
    # but not sure yet).
    def getCustomerIdOfOrder(self):
        return self.custid

    
    def getOrderType(self):
        return self.sType

    
    def getDestinationAddress(self):
        return self.destination

    
    # toString() method
    # def __str__(self):