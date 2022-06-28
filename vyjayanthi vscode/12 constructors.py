from unicodedata import name 
class A :
    # default coonstructor 
    def __init__(self):
        self.name = "vyjayanthi"
        # a mehtod for printing data members
    def print_A(self):
        print(self.name)
# creating object of the class 
obj = A()
obj.print_A()

class B(A):
    def __init__ (self):
        self.name = "KG"
    def print_B(self):
        print (self.name)

obj1 = B()
obj1.print_B()

class C:
    # public data member
    name = None
    # protected data members
    _roll = None
    # private data member
    __branch = None
    # constructor 
    def __init__(self,name,roll,branch):
        self.name = name 
        self._roll = roll 
        self.__branch =branch 
    def displayName(self):
        print("Name:",self.name)
    def _displayRoll(self):
        print("Roll",self._roll)
    def __displayBranch(self):
        print("Branch:",self.__branch)
    def access__displayBranch(self):
        self.__displayBranch()

class D(C):
    def __init__(self,name,roll,branch):
        super().__init__(name,roll,branch)
    def access_displayRoll(self):
        self._displayRoll()
obj = D("vyjayanthi",5,"CSE")
obj.displayName()
obj.access_displayRoll()
obj.access__displayBranch()














