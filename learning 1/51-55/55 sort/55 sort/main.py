# sort() method: sort lists
# sort() function: used with iterables
students = [("Joe", "S", "32"),
            ("Hun", "T", "23"),
            ("Amy", "L", "27"),
            ("Kyl", "E", "52"),
            ("Con", "B", "17")]
students_tuple = (("Joe", "S", "32"),
            ("Hun", "T", "23"),
            ("Amy", "L", "27"),
            ("Kyl", "E", "52"),
            ("Con", "B", "17"))
# students.sort(reverse=True)
# sorted_students = sorted(students, reverse=True)
# for i in sorted_students:
#     print(i)
# students.sort(key=age, reverse=True

age = lambda ages: ages[2]
sorted_students = sorted(students_tuple, key=age)
for i in sorted_students:
    print(i)
