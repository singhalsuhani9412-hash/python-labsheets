# Question 23: Write a program to swap two tuples.

t1 = (10, 20, 30)
t2 = (40, 50, 60)

t1, t2 = t2, t1

print("Tuple 1:", t1)
print("Tuple 2:", t2)

# Output:
# Tuple 1: (40, 50, 60)
# Tuple 2: (10, 20, 30)