# Question 25: Write a program to find the difference between two tuples.

t1 = (10, 20, 30, 40)
t2 = (30, 40, 50, 60)

difference = tuple(x for x in t1 if x not in t2)

print("Difference:", difference)

# Output:
# Difference: (10, 20)