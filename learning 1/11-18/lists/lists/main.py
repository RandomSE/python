'''
dinner = ["lasagne", "spaghetti", "salad"]
drinks = ["water", "soda", "lemonade"]
dessert = ["chocolate", "ice cream", "raspberry"]
foods = [dinner, drinks, dessert]

foods[2] = "hamburger"
foods.append("pizza")
foods.pop()
foods.sort()

print(foods[0][0])

'''

student = ("Devin", "23", "male")

utensils = {"Spoon", "Knife", "Fork"}
dishes = {"Bowl", "Plate", "Cup"}
utensils.add("Spork")
# utensils.update(dishes)
# table = utensils.union(dishes)
# for x in table:
    # print(x)
print(dishes.intersection(utensils))

