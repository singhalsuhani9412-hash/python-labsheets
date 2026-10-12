# Question 29: Find common keys between two dictionaries.

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 40}

common_keys = dict1.keys() & dict2.keys()

print("Common Keys:", common_keys)