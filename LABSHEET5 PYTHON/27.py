# Question 27: Write a program to unzip a list of tuples into individual lists.

t = [(1, "A"), (2, "B"), (3, "C")]

numbers, letters = zip(*t)

print("Numbers:", list(numbers))
print("Letters:", list(letters))

# Output:
# Numbers: [1, 2, 3]
# Letters: ['A', 'B', 'C']