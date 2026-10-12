# Question 24: Write a program to find common elements between two tuples.

t1 = (10, 20, 30, 40)
t2 = (30, 40, 50, 60)

common = tuple(x for x in t1 if x in t2)

print("Common Elements:", common)

# Output:
# Common Elements: (30, 40)