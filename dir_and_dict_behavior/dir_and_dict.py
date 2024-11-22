class MyVariable():
    x = 3
    
    def __init__(self):
        self.x = 4
        self.y = 5
    
    def foo(self):
        x = 6
        return x

if __name__ == '__main__':

    first = MyVariable() # Line A
    
    first.z = 7
    
    print(dir(MyVariable)) # Line 1
    '''
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'foo', 'x']
    '''
    
    print(MyVariable.__dict__) # Line 2
    '''
    {'__module__': '__main__', 'x': 3, '__init__': <function MyVariable.__init__ at 0x7fca4680cc20>, 'foo': <function MyVariable.foo at 0x7fca4680ce00>, '__dict__': <attribute '__dict__' of 'MyVariable' objects>, '__weakref__': <attribute '__weakref__' of 'MyVariable' objects>, '__doc__': None}
    '''
    
    print(dir(first)) # Line 3
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'foo', 'x', 'y', 'z']
    
    print(first.__dict__) # Line 4
    {'x': 4, 'y': 5, 'z': 7}
    
    print(first.x) # Line 5
    4
