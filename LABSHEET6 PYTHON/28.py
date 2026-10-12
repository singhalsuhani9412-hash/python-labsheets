# Q28. Write a program to create a frozen set and demonstrate its properties.

my_set = frozenset([10, 20, 30, 40])

print("Frozen set:", my_set)
print("Length:", len(my_set))
print("Is 20 present?", 20 in my_set)

# Output (frozen set order may vary):
# Frozen set: frozenset({40, 10, 20, 30})
# Length: 4
# Is 20 present? True