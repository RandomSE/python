from car import Car, car_interface
from animals import Animal, Rabbit, Fish, Hawk, Moose
# OOP with basic defines, could add more choices/ customization for cars.
car_instance = Car("Chevy", "Lightweight", 1997, "turquoise")  # can be changed
car_interface(car_instance)
rabbit_instance = Rabbit("Mr carrot")
fish_instance = Fish("Cape Cod")
hawk_instance = Hawk("Dennis the menace")
moose_instance = Moose("Heavyweight champion")
Moose.swim(moose_instance)
Animal.fight(rabbit_instance, fish_instance)  # make whichever ones fight
