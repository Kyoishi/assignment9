
from functools import reduce

list = [3,5,8,1]

def product_of_odds(list):
    return reduce(lambda x,y: x*y, filter(lambda x: x%2 ==1, list))
        # map(map_function, list)))

print(product_of_odds(list))