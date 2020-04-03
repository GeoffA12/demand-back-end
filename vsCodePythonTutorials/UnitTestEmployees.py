import unittest
import Employee
import techEmployee
import businessEmployee

# Sample unit test case suite for the business employee and tech employee subclasses we made.
class Test_Employees(unittest.TestCase):

    # Test getters of a normal tech employee instance
    # constructor of TechEmployee: __init__(self, name, id)
    def testTechEmployeeJim(self):
        e = techEmployee.TechEmployee("Jim", 3)
        self.assertEqual(e.getName(), "Jim")
        self.assertEqual(e.getSalary(), techEmployee.TechEmployee.salary)
        self.assertEqual(e.getCheckIns(), 0)
        self.assertEqual(e.getID(), 3)

    def testTechEmployeeLiam(self):
        e = techEmployee.TechEmployee("Liam", 5)
        self.assertEqual(e.getName(), "Liam")
        self.assertEqual(e.getSalary(), techEmployee.TechEmployee.salary)
        self.assertEqual(e.getCheckIns(), 0)
        self.assertEqual(e.getID(), 5)

    def testBadTechEmployeeBadCheckIns(self):
        e = techEmployee.TechEmployee("Marcus", 0)
        self.assertEqual(e.getName(), "Marcus")
        self.assertEqual(e.getSalary(), techEmployee.TechEmployee.salary)
        with self.assertRaises(AssertionError):
            self.assertEqual(e.getCheckIns(), 2)

    def testBadTechEmployeeBadSalary(self):
        e = techEmployee.TechEmployee("Baker", 6)
        self.assertEqual(e.getName(), "Baker")
        with self.assertRaises(AssertionError):
            self.assertEqual(e.getSalary(), 50000.00)

    def testBusinessEmployee(self):
        b = businessEmployee.BusinessEmployee("Marsha", 5.00, 7)
        self.assertEqual(b.getName(), "Marsha")
        self.assertEqual(b.getID(), 7)
        self.assertEqual(b.getSalary(), businessEmployee.BusinessEmployee.salary)
        self.assertEqual(b.getBonus(), 5.00)
    
    def testBusinessEmployeeBadBonus(self):
        b = businessEmployee.BusinessEmployee("Tammy", 15.00, 7)
        self.assertEqual(b.getName(), "Tammy")
        self.assertEqual(b.getID(), 7)
        self.assertEqual(b.getSalary(), businessEmployee.BusinessEmployee.salary)
        with self.assertRaises(AssertionError):
            self.assertEqual(b.getBonus(), 5.00)

    

if __name__ == "__main__":
    unittest.main()

