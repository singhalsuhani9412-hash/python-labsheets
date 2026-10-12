# Question 5: Create a list of squares of numbers from 1 to n.

n = 5

squares = []

for x in range(1, n + 1):
    squares.append(x ** 2)

print("Squares:", squares)