from re import sub


class Super:
    var1 = None
    _var2 = None
    __var3 = None 

def __init__(self,var1,var2,var3):
    self.var1 = var1
    self._var2= var2
    self.__var3 = var3

    def displaypublicMembers(self):
        print("Public Data Member :",self._var1)
    
    def _displayProtectdMembers(self) :
        print("Protected Data Member:",self._var2)

    def _displayPrivateMembers(self):
        print("Private Data Member:",self.__var3)

    def accessPrivateMembers(self):
        self.__displayPrivateMembers()

class Sub(Super):
      def __init__(self,var1,var2,var3):
               Super.__init__(self,var1,var2,var3)
    
      def accessProtectedMembers(self):
                self._displayProtectedMembers()

obj = Sub("KG", 5 , "KG!")

obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

print("object is accessing protected member:",obj._var2)