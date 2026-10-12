# Q25. Write a program to find common letters in two strings using sets.

string1 = "hello"
string2 = "world"

common_letters = set(string1) & set(string2)
print("Common letters:", common_letters)

# Output (order may vary):
# Common letters: {'l', 'o'}