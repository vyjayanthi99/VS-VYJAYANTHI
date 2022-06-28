from abc import ABC , abstractmethod 
class polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass 
class Triangle(polygon):
    # overriding abstract method
    def noofsides(self):
        print("Triangle:I have 3 sides")
class pentagon(polygon):
    # overriding abstract method
    def noofsides(self):
        print("pentagon:I have 5 sides")

class Hexagon(polygon):

# overriding abstract method
    def noofsides(self):
        print("Hexagon:I have 6 sides")

class Quadrilateral (polygon):
    # overriding abstract method
    def noofsides(self):
        print("Quadrilateral:I have 4 sides")

# Driver code 
# creating the objects to call the abstract method 
R =Triangle()
R.noofsides()
K = Quadrilateral()
K.noofsides()
R = pentagon()
R.noofsides()
K=Hexagon()
K.noofsides()


    


