# Question 21: Find the key with the maximum value in a dictionary.

marks = {"Aman": 80, "Riya": 95, "Rahul": 70}

top_student = max(marks, key=marks.get)

print("Student with Maximum Marks:", top_student)
print("Maximum Marks:", marks[top_student])