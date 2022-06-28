class A():
    def display(dp):
        print("Display Inside class A")

    def show(self):
        print("Show Inside class A")

class B (A):
    def print(pt) :
        print("print Inside class B")

    def show(self):
         print("Show Inside class B")

class C(B):

    def show(self):
        print("Show Inside class C")
# Driver code
s = A()
s.display()
k = B()
k.print()
g = C()
g.show()
