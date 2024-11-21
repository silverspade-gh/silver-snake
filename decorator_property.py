# decorator_property.py
# An example of the built-in decorator that helps define read-only attributes.

class MyClass:
    def __init__(self):
        self._read_only_attr = 10  # Leading underscore implies protected access

    @property
    def read_only_attr(self):
        return self._read_only_attr  # No setter defined, making it read-only

obj = MyClass()
print(obj.read_only_attr)  # Output: 10

# Attempting to modify this will raise an AttributeError
# obj.read_only_attr = 20  # This line would cause an error
# obj._read_only_attr = 20  # This line is OK
