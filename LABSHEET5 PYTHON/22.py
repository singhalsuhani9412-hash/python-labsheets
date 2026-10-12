# Question 22: Write a program to flatten a nested tuple.

t = ((1, 2), (3, 4), (5, 6))

result = tuple(item for subtuple in t for item in subtuple)

print("Flattened Tuple:", result)

# Output:
# Flattened Tuple: (1, 2, 3, 4, 5, 6)