class Animal:

    def eat(self):
        print("This animal is eating")


class Rabbit(Animal):
    def eat(self):  # overriding
        print("This rabbit is eating rabbit food.")


rabbit = Rabbit()
rabbit.eat()
