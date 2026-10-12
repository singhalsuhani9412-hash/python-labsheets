# Question 3: Remove all negative numbers from a list.

numbers = [10, -5, 20, -8, 30, -2]

result = [x for x in numbers if x >= 0]

print("Original list:", numbers)
print("List after removing negative numbers:", result)