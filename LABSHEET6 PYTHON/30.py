# Q30. Write a program to perform all basic set operations
# (union, intersection, difference, symmetric difference) in one program.

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

# Output (set order may vary):
# Union: {10, 20, 30, 40, 50, 60}
# Intersection: {30, 40}
# Difference: {10, 20}
# Symmetric Difference: {10, 20, 50, 60}