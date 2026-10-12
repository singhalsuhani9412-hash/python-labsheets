# Question 24: Invert a dictionary.

data = {"Aman": 1, "Riya": 2, "Rahul": 3}

inverted = {}

for key, value in data.items():
    inverted[value] = key

print("Inverted Dictionary:", inverted)