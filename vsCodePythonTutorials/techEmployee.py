# We need to import the Employee class FROM the Employee module. 
from Employee import Employee

# TechEmployee subclass which inherits from the Employee class. Notice that we do need to specify the 
# Employee class inside the parentheses of our class definition. 
# A TechEmployee will have a specific checkIns integer attribute which will always be instantiated to a value of 0.
class TechEmployee(Employee):
    # Defining a class variable here. 
    salary = 75000.00
    def __init__(self, name, id):
        # This is how we utilize inheritance in the subclass constructor. What this line below will do is take the data
        # from the user, (name, id), and pass it along with a constant value (TechEmployee.salary) defined on line 9, and then
        # call the superclass Employee parent constructor. Notice that we do need to also pass 'self' in this constructor call as well. 
        Employee.__init__(self, name, TechEmployee.salary, id)
        self.__checkIns = 0
    
    def getCheckIns(self):
        return self.__checkIns
    
    # Override the getEmployeeStatus() method defined in the Employee superclass.
    def getEmployeeStatus(self):
        return Employee.__str__(self) + " and I have " + self.getCheckIns() + " check ins."

    


