RandomGroup = {"type": "extreme", "Brand": "Coyote", "Why": "Because. "}


# print(RandomGroup)


def greet(name):
    print("Good day " + name + "!")


# greet("Andrew")

# basic addition
'''
def add_numbers(a, b):
    return a + b


k = int(input("input a number"))
L = int(input("Input a second number"))
result = add_numbers(k, L)
print(result)
'''

# string indexing and slicing
'''
Full_name = "Andrew Romanos"
First_name = Full_name[:6]
Last_Name = Full_name[7:]
Chunky_Name = "J1e2r3e4m5y"
Reversed_name = Full_name[::-1]
Less_name = Chunky_Name[::2]

greet(First_name + " " + Last_Name)  # used here, splitting waste.
greet(Less_name)
print("why. " + Reversed_name)

domain1 = "https://www.youtube.com"
domain2 = "https://www.github.com"
slice = slice(12, -4)
print(domain1[slice])
print(domain2[slice])
'''

age = int(input("How old are you?"))
if age >= 123:
    print("You are the oldest person alive!")
elif age >= 18:
    print("You are an adult")
elif age < 0:
    print("You are not yet born.")
else:
    print("You are a child.")


temp = round(int(input("What is the temperature outside?")))
if -10 < temp <= 0:
    print("it's coldoutside!")
elif 0 < temp <= 20:  # simplified and
    print("The temperature is nice today.")
elif temp > 20 or temp < -10:
    print("The weather is chaotic outside.")  # I am not a fan of warm weather
