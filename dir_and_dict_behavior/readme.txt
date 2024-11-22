Line 1

This returns the namespace including built-in and user-defined attributes, methods and functions of the class MyVariable.

Line 2

This includes writable attributes for MyVariable. Notice that the attributes defined in the methods and functions are not included. Those do not exist unless the respective function is called: An implicit creation occurs in Line A for first.y, and an explicit creation for x in MyVariable().foo().

Line 3

This is the same output as Line 1 but with instance attributes added. This is the expected behavior as described in the previous list of bullet points regarding dir(). The object inherits the class namespace. The x in this namespace refers to self.x (see line 5 for more details).

Line 4

These are the writable attributes for the first object of type MyVariable. Methods such as foo are not included because all instances share them, unless explicitly overridden for that particular object.

Line 5

When first.x is called, it could be referring to the MyVariable.x or self.x. But which x it refers to depends on its locality. 

Because the object constructor is nested within the class, then x equals 4. It does not use the x inside MyVariable().foo() either because, although it's most nested in the class, it would be local to the function.
