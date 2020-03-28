# Testing Comment from ssh cloned repo
# Python demand customer class. 
# Note that if we decide to use inheritance in this class defintion, (e.g., customer extends User),
# then we'll need to change our class defintion below
class Customer():

    # Class constructor. Set instance variables below. 
    def __init__(self, username, password, email, phone):
        self.__username = username
        self.__password = password
        self.__email = email
        self.__phone = phone
        
    #Defining our getter methods
    def getUsername(self):
        return self.__username
        

    def getPassword(self):
        return self.__password

    
    def getEmail(self):
        return self.__email

    
    def getPhone(self):
        return self.__phone

    
    # toString() method
    def __str__(self):
        return self.getUsername() + " " + self.getPassword() + " " + self.getEmail() + " " + self.getPhone()
        
    def getCustomerInfo(self):
        return self.__str__
