# Question 10: Convert a list into a string without using join().

items = ['Python', 'is', 'easy']

result = ""

for item in items:
    result = result + item + " "

print("String:", result.strip())