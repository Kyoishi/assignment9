
from functools import reduce

# Write a function that determines 
# the maximum value from a list of numerical values.

def max_number(list_of_numbers):
    
    max = 0
    for i in list_of_numbers:
        if i > max:
            max = i
        else:
            pass
    
    return max

list = [1,10,20,3,4]
print(max_number(list))


# Write a statement using reduce that also determines 
# the maximum value of a list of numerical values.

max = reduce(lambda x,y: max(x,y), list)
print(max)

# Compare the two approaches in terms of the time complexity. 
# 1st one: O(n^2), 2nd one: O(n)
