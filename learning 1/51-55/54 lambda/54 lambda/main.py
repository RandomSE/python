# lambda function: function written in 1 line using lambda keyword. accept any number of arguments, only has 1 express


double = lambda x: x*2
multiply = lambda x, y: x*y
add = lambda x, y, z: x + y + z
age_check = lambda age: True if age >= 18 else False
print(age_check(12))
