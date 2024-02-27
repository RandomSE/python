# walrus operator :=   -> assigns values to variables as part of a larger expression

print(happy := True)  # happy = True + print(happy)

foods = list()
'''
while True:
    food = input("What food do you like?").strip().lower()
    foods.append(food := input("What food do you like?").strip)
    if food == "quit":
        break
    foods.append(food)
'''
# the given code in the video doesn't work properly: food is = True, not the value in input.
numbers = [1, 2, 3, 4, 5]
squared_numbers = [square for n in numbers if (square := n ** 2) and n % 2 == 0]
print(squared_numbers)
