# filter() creates collection of elements from an iterable for which a function returns True #filter(function,iterable)
acquaintances = [("Jan", 89),
                 ("Jen", 23),
                 ("Ren", 33),
                 ("Amy", 27),
                 ("Cro", 44),
                 ("Met", 17)]
age = lambda data: data[1] >= 18
of_age = list(filter(age, acquaintances))
for i in of_age:
    print(i)
