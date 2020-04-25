import sys

if '../' in sys.path[1]:
    sys.path[1] = sys.path[1] + '../common-services'
else:
    sys.path.insert(1, '../common-services')

from account import Account

# Python Demand Customer Class
class Customer(Account):

    # Class constructor. Set instance variables below. 
    def __init__(self, username, email, password, firstname, lastname, phonenumber):
        super().__init__(username, email, password, firstname, lastname, phonenumber)
        #self.custIDs = self.__fetchAssociatedCustIDs()
        
    # def __fetchAssociatedCustIDs(self):
    #     print()
    #     return 'tbd'
    
    # @property
    # def custIDs(self):
    #     return self.custIDs
    
    # toString() method
    def __str__(self):
        return "Username: " + self._username + " Email: " + self._email + " Password: " + self._password + " First Name: " + self._firstname + " Last Name: " + self._lastname + " Phone Number: " + self._phonenumber

