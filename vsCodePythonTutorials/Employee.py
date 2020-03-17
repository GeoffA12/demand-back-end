# OOP in Python

# Employee will be our superclass definition in this module. Each employee instance will have a name, 
# salary, and id. There are two subclasses, techEmployee and businessEmployee, which inherit from Employee. 
class Employee:
    # Our class constructor definition
    def __init__(self, name, salary, id):
        ## These are our instance variables. Two underscore characters to the right of the 'self.' means that this 
        ## instance variable is private.
        self.__name = name
        self.__salary = salary
        self.__id = id

    # Defining our getter methods for our superclass
    def getName(self):
        return self.__name
    
    def getSalary(self):
        return self.__salary
    
    def getID(self):
        return self.__id
    
    # Override the equals method. By default, using the == operator between two python objects will 
    # only check the memory reference adress of the instance 
    def __eq__(self, employee2):
        same = True
        if (isinstance(employee2, self)):
            if (employee2.getSalary() != self.getSalary() or employee2.getName() != self.getName()):
                same = False

        else:
            same = False
        return same

    # This is how you write a toString() method for your python class. 
    def __str__(self):
        return self.getID() + " " + self.getName()

    def getEmployeeStatus(self):
        return self.__str__

        



    
