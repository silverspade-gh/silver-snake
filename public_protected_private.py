# public_protected_private.py
# A demonstration of how Python adapts the variable accessibility features seen in C++.

class C1():
    def __init__(self):
        self.w = '3' # This is a normal attribute. Nothing interesting happens.
        self._w = '4' # No special behavior occurs, but humans see the single underscore
        self.__w = '5' # The interpreter recognizes the double underscore and 'mangles' the name
        
class C2(C1):
    def __init__(self):
        super().__init__()
        
if __name__ == '__main__':
    c1 = C1()
    print(c1.w) # Prints 3
    print(c1._w) # Prints 4
    print(c1.__w) # Attribute error: The name doesn't exist.
    print(c1._C1__w) # This is the new name of the attribute.
    
    c2 = C2() # All attributes are inherited due to the use of the super() constructor
    print(c2.w) # Prints 3
    print(c2._w) # Prints 4
    print(c2.__w) # Attribute error: The name doesn't exist (just as above).
    print(c2._C1__w) # This is the new name of the attribute (just as above). Prints 5.
