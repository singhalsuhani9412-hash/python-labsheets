# Question 13: Count the frequency of characters in a string using a dictionary.

text = "hello"
frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character Frequency:", frequency)