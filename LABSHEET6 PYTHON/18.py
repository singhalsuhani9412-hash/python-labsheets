# Q18. Write a program to remove all elements of one set from another set.

set1 = {10, 20, 30, 40, 50}
set2 = {20, 40}

set1.difference_update(set2)
print("Updated set:", set1)

# Output:
# Updated set: {10, 30, 50}