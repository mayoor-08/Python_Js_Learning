class Pen:

    def __init__(self, color, size, inkType, manufacturer) -> None:
        
        self.color = color
        # Protected
        self._inkFormula = "H2So4"
        # private
        # Name Mangaling : will convert first _ into _ClassName_ internally
        self.__companyRevenue = 25
        # print("color = ", self.color)
        self.size = size
        self.inkType = inkType
        self.manufacturer = manufacturer
        # print("self",self)


    def displayPen(self):
        print("color :", self.color)
        print("size :", self.size)
        print("ink type :", self.inkType)
        print("manufacturer :", self.manufacturer)

    def _test(self):
        print("Hello world")
        print(self.__companyRevenue)


class Refill(Pen):
    def refill(self):
        print(self._inkFormula)
        print(self._test())





pen1 = Pen("black", "thin","gel","reynolds")
# print(pen1)
# print(pen1.color)
# print(pen1.size)
# print(pen1.inkType)
# print(pen1.manufacturer)

# Object Attributes
# print(vars(pen1))
# print(dir(pen1))
# pen1.displayPen()

# pen1.color = "red"
# pen1.displayPen()

# pen2 = Pen("blue","thin","ball","flair")
# pen2.displayPen()
# print(pen2.color)
# print(pen2.size)
# print(pen2.inkType)
# print(pen2.manufacturer)
# print(Pen.__dict__)
# print(pen1.__dict__)

# print(pen1.Pen_companyRevenue)

# print(pen1._test())
r = Refill("black", "thin","gel","reynolds")

# r.refill()
# # r.test()
print(vars(r))
# print(r._Pen__companyRevenue)

print(r._inkFormula)
print(r._Pen__companyRevenue)