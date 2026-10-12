# Q26. Write a program to find unique words in a sentence using a set.

sentence = "python is easy and python is powerful"
words = set(sentence.split())

print("Unique words:", words)
print("Number of unique words:", len(words))

# Output (set order may vary):
# Unique words: {'python', 'is', 'easy', 'and', 'powerful'}
# Number of unique words: 5