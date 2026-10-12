# Question 20: Write a program to find the length of the longest word in a tuple.

t = ("Python", "Java", "Programming", "HTML")

longest_length = max(len(word) for word in t)

print("Length of longest word:", longest_length)

# Output:
# Length of longest word: 11