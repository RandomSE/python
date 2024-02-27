
class Car:
    color = None


class Motorcycle:
    color = None


def change_color(vehicle, color):
    vehicle.color = color


car_1 = Car()
car_2 = Car()
car_3 = Car()
motorcycle_1 = Motorcycle()

change_color(car_1, "orange")
change_color(car_2, "teal")
change_color(car_3, "black")
change_color(motorcycle_1, "silver")
print(car_1.color)
print(car_2.color)
print(car_3.color)
print(motorcycle_1.color)