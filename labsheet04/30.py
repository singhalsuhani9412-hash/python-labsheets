# Question 30: Create a dictionary from a string with characters as keys and frequency as values.

text = "programming"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character Frequency:", frequency)