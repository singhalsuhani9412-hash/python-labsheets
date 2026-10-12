# Question 9: Flatten a nested list.

nested_list = [[1, 2], [3, 4], [5, 6]]

flat_list = []

for sublist in nested_list:
    for x in sublist:
        flat_list.append(x)

print("Nested list:", nested_list)
print("Flattened list:", flat_list)