
# Use the following list of temperature on each of your approaches:
temperatures = [-32.0, 0.0, 1.0, 10.0, 32.0, 50.3, 88.8, 101.0]

# Write a statement using map that takes a list of temperatures in Celsius
# and converts then to Fahrenheit.

def converter(x):
    return x * 9/5 + 32

converted = map(converter, temperatures)
print(converted)

# Write another statement using list comprehension
# to make the same conversion.

converted_temps = [(x * 9/5 + 32) for x in temperatures]
print(converted_temps)

# What is the time complexity of each approach? 
# Answer: both of the statements are  

# Devise and conduct a benchmarking experiment to determine if one is faster than the other in practice.