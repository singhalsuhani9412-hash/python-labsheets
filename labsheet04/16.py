# Question 16: Sort a dictionary by values.

data = {"Aman": 85, "Riya": 95, "Rahul": 75}

sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

print("Sorted Dictionary:", sorted_data)