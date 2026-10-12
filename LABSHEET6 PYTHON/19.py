# Q19. Write a program to create the power set of a given set.

from itertools import combinations

my_set = {1, 2, 3}
power_set = []

for i in range(len(my_set) + 1):
    for subset in combinations(sorted(my_set), i):
        power_set.append(set(subset))

print("Power set:", power_set)

# Output:
# Power set: [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]