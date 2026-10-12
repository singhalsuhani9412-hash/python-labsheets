# Question 30: Write a program to find the element-wise sum of two tuples.

t1 = (10, 20, 30)
t2 = (40, 50, 60)

result = tuple(a + b for a, b in zip(t1, t2))

print("Element-wise Sum:", result)

# Output:
# Element-wise Sum: (50, 70, 90)