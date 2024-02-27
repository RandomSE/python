import math
name = "roleth"


# print(len(name))
# print(name.find('l'))
# print(name.upper())
# print(name.lower())
# print(name.isalpha())
# print(name.isnumeric())
# print(name.isdigit())
# print(name.count('e'))
# print(name.replace("r", "o"))
# print((name + ' ') * 3)


# type casting
x, y, z = 7, 0.33, "12"


int(round(y, 2))
str(x)
z = int(z)

# print(x)
# print(z * 3)
# print(y)

NewName = input("What is your name?")

if len(NewName) > 0:
    print("Your name is: " + NewName)


if 1 > len(NewName) > -1:  # error when trying if len(NewName) = 0:
    print("You did not enter a name")

DigitCheck = True

Age = input("What will your age be at the end of 2024?")
if not Age.isdigit:
    DigitCheck = False
    print("The input must be in digits only.")
    Age = input("What will your age be at the end of 2024?")
    # not learn loops yet, and while/until loops do not work in python...?
iYear = 2024


if Age.isdigit:
    BirthYear = iYear - int(Age)
    print("You were born in: " + str(BirthYear))


height = input("What is your height in CM?")
print("You are :" + str(height) + "CM tall.")


pi = 3.141519
#  print(round(pi, 3))
#  print(math.ceil(pi))
#  print(abs(pi))
#  print(pow(pi, 2))

xn, yn, zn = 10, 13, 2
print(max(xn, yn, zn))


