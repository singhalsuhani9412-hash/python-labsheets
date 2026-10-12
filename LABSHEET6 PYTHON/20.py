# Q20. Write a program to find the Cartesian product of two sets.

set1 = {1, 2}
set2 = {'A', 'B'}

result = {(x, y) for x in set1 for y in set2}
print("Cartesian product:", result)

# Output (one possible order):
# Cartesian product: {(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')}