# list comprehension: a way to create a new list with less syntax. can also be used to mimic certain lambda functions.
# list = [expression for item in iterable]


squares = [i * i for i in range(1, 11)]
print(squares)


students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
# passed_students = [i for i in students if i >= 60]
passed_students = [i if i >= 60 else "Failed" for i in students]
print(passed_students)
