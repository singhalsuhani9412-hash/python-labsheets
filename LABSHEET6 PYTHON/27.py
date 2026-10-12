# Q27. Write a program to check if two strings are anagrams using sets.

string1 = "listen"
string2 = "silent"

if set(string1) == set(string2) and len(string1) == len(string2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")

# Output:
# Strings are anagrams