'''
capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
# print(capitals["Russia"])
# print(capitals.get("Germany"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
capitals.update({"Germany": "Berlin"})
capitals.pop("Russia")
for key, value in capitals.items():
    print(key, value)


name = "dodge Chevrolet"
if name[0].islower():
    name = name.capitalize()
print(name)

First_name = name[0: 5].upper()
Last_name = name[6:].lower()
print(Last_name)




def greeting(name1):
    first = "Hello, "  # for local scope
    last = "!"
    print(first + name1 + last)


name = input("What is your name?")
while name == "":  # while name is None does not work
    name = input("What is your name?")

greeting(name)


def multiply(number1, number2):
    return number1 * number2


x = multiply(7, 12)
print(x)


print(round(abs(float(input("put a whole number.")))))




#
def add(*stuff):  # * is very important, the name is not. Makes into a tuple.
    total = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        total += i
    return total + 1


print(add(1, 2, 3, 4, 5, 6, 7, 8))


# accidentally did string formats before kwargs
Number = 1000
print("To 3 decimals: {:.3f}".format(Number))
print("with a comma: {:,}".format(Number))
print("In binary: {:b}".format(Number))
print("...?: {:o}".format(Number))
print("More letters...? : {:X}".format(Number))
print("In scientific notation: {:e}".format(Number))


'''


def hello(**kwargs):
    print("Hello,", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(Title="Thee", First="Jasmine", Middle="Sort of", Last="Rice")
