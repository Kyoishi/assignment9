
numbers = [1,3,5]

# Snippet 1
map(lambda x: x ** 2, numbers)
# answer: O(n)

# Snippet 2
filter(lambda x: x % 2, numbers)
# answer: O(n)

# Snippet 3
reduce(lambda x,y: x + y, numbers)
# answer: O(n)