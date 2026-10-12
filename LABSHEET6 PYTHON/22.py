# Q22. Write a program to find duplicate elements in a list using a set.

my_list = [10, 20, 30, 20, 40, 10, 50, 30]

seen = set()
duplicates = set()

for element in my_list:
    if element in seen:
        duplicates.add(element)
    else:
        seen.add(element)

print("Duplicate elements:", duplicates)

# Output (set order may vary):
# Duplicate elements: {10, 20, 30}