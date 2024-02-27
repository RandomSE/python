
# multiple inheritance, seems that / in name is a new folder...?
class Prey:
    name1 = "Prey"  # otherwise fish just does predator and predator for the names.

    def flee(self):
        print(self.name1 + " flees from a predator")


class Predator:
    name = "Predator"

    def hunt(self):
        print(self.name + " hunts their prey")


class Turtles(Prey):
    pass


class Lions(Predator):
    pass


class Fishes(Predator, Prey):
    pass


turtle = Turtles()
lion = Lions()
fish = Fishes()

fish.hunt()
fish.flee()
