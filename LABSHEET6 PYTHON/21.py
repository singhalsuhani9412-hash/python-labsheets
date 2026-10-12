# Q21. Write a program to count distinct elements from a list using a set.

my_list = [10, 20, 10, 30, 20, 40, 50]

distinct_elements = set(my_list)
print("Distinct elements:", distinct_elements)
print("Count of distinct elements:", len(distinct_elements))

# Output (set order may vary):
# Distinct elements: {40, 10, 50, 20, 30}
# Count of distinct elements: 5