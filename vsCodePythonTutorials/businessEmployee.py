from Employee import Employee

class BusinessEmployee(Employee):
    # Constant class variable that we'll utilize in the constructor call. Note that class variables are accessible from anywhere in our class
    # Even if we import this class to another file we will still have 'public' access to this variable
    salary = 50000.00
    def __init__(self, name, bonus, id):
        # This is how we utilize inheritance in the subclass constructor. What this line below will do is take the data
        # from the user, (name, bonus, id), and pass it along with a constant value (BusinessEmployee.salary) defined on line 4, and then
        # call the superclass Employee parent constructor. Notice that we do need to also pass 'self' in this constructor call as well. 
        Employee.__init__(self, name, BusinessEmployee.salary, id)
        self.__bonus = bonus
    
    def getBonus(self):
        return self.__bonus

     # Override the getEmployeeStatus() method defined in the Employee superclass.
    def getEmployeeStatus(self):
        return Employee.__str__(self) + " and I have a bonus budget of " + self.getBonus()
