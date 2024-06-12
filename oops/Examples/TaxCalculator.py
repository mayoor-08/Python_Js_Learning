class TaxCalculator:
    def __init__(self, data) -> None:
        self.isTaxable = None
        self.tax = None
        self.salary = data["salary"]
        self.profile = data


    def testIsTaxable(self):
        if self.salary > 10000:
            self.isTaxable = True
            return True
        
        self.isTaxable = False
        return False
    
    def calculateTax(self):
        if self.isTaxable == None:
            self.testIsTaxable()

        if self.isTaxable:
            self.tax = int(self.salary *.1)
            return True
        self.tax = 0
        return False
    
    def showProfile(self):
        if self.isTaxable == None:
            self.testIsTaxable()
        if self.tax == None:
            self.calculateTax()
        self.profile["tax"] = self.tax
        self.profile["total"] = self.salary + self.tax

        return self.profile
        


data = {"name" : "Ram", "age" : 25, "salary": 12000}
emp1 = TaxCalculator(data)
print(emp1.isTaxable)
print(emp1.tax)
print(emp1.salary)
print(emp1.profile)
print(emp1.showProfile())
emp1.calculateTax()
emp1.testIsTaxable()
print(emp1.isTaxable)
print(emp1.tax)
