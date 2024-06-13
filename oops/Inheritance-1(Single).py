class Parent:

    _counter = 0

    def __init__(self, salutation) -> None:
        print(f"{salutation} from parent initializer")

    def printWorld(self):
        return "Hello World from Parent"



class Child(Parent):

    def __init__(self, salutation="hello") -> None:
        print(f"{salutation} Word from Child initializer")

    def counterIncrement(self):
        self._counter += 1

    def printCounter(self):
        print(self._counter)


class GrandChild(Child):

    # def __init__(self, salutation) -> None:
    #     print(f"{salutation} from grand child initializer")
    pass



# c1 = Child()
# c1.printWorld()
# c1.counterIncrement()
# c1.counterIncrement()
# c1.counterIncrement()
# c1.counterIncrement()
# c1.counterIncrement()
# c1.counterIncrement()
# c1.counterIncrement()
# c1.counterIncrement()
# c1.counterIncrement()
# print(type(c1))

# p1= Parent()
# print(type(p1))
# print(p1.printWorld())

gc = GrandChild(salutation="bye")



