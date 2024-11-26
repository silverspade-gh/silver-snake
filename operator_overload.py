# car.py
# Describes the behavior of a car, the fill function and 
# overloading the addition (+) operator to promote built-in behavior.

class Car():
    def __init__(self, amount_of_gas, tank_size):
    
        self.__tank_size = tank_size
        
        if self.__tank_size < amount_of_gas:
            self.__gas = tank_size # You cannot overfill the tank!
        else:
            self.__gas = amount_of_gas
        
    # This will be name-mangled to promote encapsulation
    def __fill_tank(self, amount_of_gas):
        if self.__tank_size < self.__gas + amount_of_gas:
            self.__gas = self.__tank_size # You cannot overfill the tank!
        else:
            self.__gas += amount_of_gas 
            
    # Here we now overload the + operator by overloading __add__():
    def __add__(self, amount_of_gas):
        self.__fill_tank(amount_of_gas)
        
        # We want to modify the original object,
        # not create and return a new one.
        return self
        
    # Defining the string representation of the object
    # so print() returns a valid, human-readable description
    # as an f-string
    def __str__(self):
        return (f'This is a car with {self.__gas} units for gas and '
        f'{self.__tank_size} units of capacity for gas.')
        
if __name__ == '__main__':
    my_car = Car(5, 10)
    my_car += 3
    print(my_car)
    
    # This will raise an error
    # my_car.fill_tank(6)
    
    # This is OK, but no one would write this.
    # This is the same as my_car += 6
    # or my_car = my_car + 6
    # or, in non-name-mangled programs, my_car.fill_tank(6)
    my_car._Car__fill_tank(6)
