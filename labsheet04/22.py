# Question 22: Create a dictionary with numbers as keys and their squares as values.

n = 5

squares = {}

for x in range(1, n + 1):
    squares[x] = x ** 2

print("Squares Dictionary:", squares)