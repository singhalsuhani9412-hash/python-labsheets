# Question 28: Write a program to find repeated items in a tuple.

t = (10, 20, 10, 30, 20, 40, 10)

repeated = tuple(x for x in dict.fromkeys(t) if t.count(x) > 1)

print("Repeated Items:", repeated)

# Output:
# Repeated Items: (10, 20)