class Animal:
    alive = True
    name = "animal"
    strength = 300  # ... why am I coding a combat system. Either way, it is unrealistic.

    def eat(self):
        print("This " + self.name + " is eating")

    def sleep(self):
        print("This " + self.name + " is sleeping")

    def fight(self, opponent):
        print(f"{self.name} is fighting {opponent.name}")
        if self.strength > opponent.strength:
            print(f"{self.name} wins!")
            opponent.alive = False
        elif self.strength < opponent.strength:
            print(f"{opponent.name} wins!")
            self.alive = False
        else:  # would only really occur with the car
            print("It's a draw!")


class Rabbit(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.strength = 150


class Fish(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.strength = 100

    def swim(self):
        print("The fish," + self.name + " swims")


class Hawk(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.strength = 300  # will win against the lightweight car going 20 km/h. Physics need not apply.

    def fly(self):
        print(self.name + " flies")


class Moose(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.strength = 1200

    def swim(self):
        print("Yes " + self.name + " Can swim.")


rabbit_instance = Rabbit("Mr carrot")
fish_instance = Fish("Cape Cod")
hawk_instance = Hawk("Dennis the menace")
moose_instance = Moose("Heavyweight champion")


# multi-level inheritance
class Organism:
    alive = True
    type = "Organism"


class Reptiles(Organism):
    def eat(self):
        print(self.type + " eats.")


class Lizards(Reptiles):
    def shed_skin(self):
        print(self.type + " Sheds it's skin")
