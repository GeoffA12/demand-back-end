import sys

if '../' in sys.path[1]:
    sys.path[1] = sys.path[1] + '../common-services'
else:
    sys.path.insert(1, '../common-services')
#print(sys.path)

from account import Account

# Testing Comment from ssh cloned repo
# Python demand customer class. 
# Note that if we decide to use inheritance in this class defintion, (e.g., customer extends User),
# then we'll need to change our class defintion below
class Customer(Account):

    # Class constructor. Set instance variables below. 
    def __init__(self, username, password, email, phone):
        super().__init__(username, password, email, phone)
        self.custIDs = self.__fetchAssociatedCustIDs()
        
    def __fetchAssociatedCustIDs(self):
        print()
        return 'yes'
    
    @property
    def custIDs(self):
        return self.custIDs
    
    # toString() method
    #def __str__(self):
        #return "Username: " self.getUsername() + " Password: " + self.getPassword() + " Email: " + self.getEmail() + " Phone Numeber: " + self.getPhone()
        
    #def getCustomerInfo(self):
        #return self.__str__
