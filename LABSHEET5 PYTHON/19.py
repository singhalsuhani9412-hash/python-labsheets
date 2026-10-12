# Question 19: Write a program to remove duplicate elements from a tuple.

t = (10, 20, 10, 30, 20, 40)

result = tuple(dict.fromkeys(t))

print("Tuple without duplicates:", result)

# Output:
# Tuple without duplicates: (10, 20, 30, 40)