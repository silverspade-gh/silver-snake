# seq_of_seq.py
# This file displays how a tuple of lists may display mutability.

a = [1]
b = [2]
c = [3]

my_tuple = (a, b, c)
print(str(my_tuple) + "'s location is " + str(id(my_tuple)))

a[0] = 4  # The list's address remains the same, so we are not altering the contents of the tuple.
          # However, the first item in the list changes! That's because lists are mutable.
          # (Same location in memory, different value...)
print(str(my_tuple) + "'s location is still " + str(id(my_tuple)))

# Result:
'''
([1], [2], [3])'s location is 140307513412800
([4], [2], [3])'s location is still 140307513412800
'''
