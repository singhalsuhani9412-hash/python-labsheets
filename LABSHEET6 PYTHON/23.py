# Q23. Write a program to remove duplicates from a list using a set.

my_list = [10, 20, 10, 30, 20, 40, 30]

result = list(set(my_list))
print("List after removing duplicates:", result)

# Output (order may vary):
# List after removing duplicates: [40, 10, 20, 30]