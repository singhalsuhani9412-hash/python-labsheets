# Question 25: Count word frequency in a paragraph using a dictionary.

paragraph = "Python is easy and Python is useful"

words = paragraph.lower().split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word Frequency:", frequency)