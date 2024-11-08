# swimming_rocks.py
# For more information on the 'self' parameter,
# refer to 9.3.4 in the docs: https://docs.python.org/3/tutorial/classes.html#method-objects

class swimming_rock:
    """A collection of rocks that can swim."""
    
    # This is a constructor.
    # It builds the rock's properties when it's instantiated!
    # If no operands are passed, the object assumes the default assignments.
    def __init__(self, color='Gray', swim_stroke='Front crawl'):
        self.color = color
        self.swim_stroke = swim_stroke
          
    # This is a procedure.
    # It can change the rock's color.
    # This couldn't be possible in the real world, but can be in Python!
    def change_color(self, new_color):
        self.color = new_color
    
    # This is a function.
    # It's a procedure that returns a value.
    def talk(self):
    
        # I wouldn't want my rock talking, so it returns an empty string!
        return ''

# By including this common conditional, the code will only run
# if the file is run as is (i.e., python swimming_rocks.py)
# and not as an imported module (i.e., import swimming_rocks).       
if __name__ == '__main__':
    my_pet_rock = swimming_rock()
    
    # This is equivalent to swimming_rock.talk(my_pet_rock)
    # as documented in 9.3.4 on the 'self' parameter.
    print(my_pet_rock.talk())
