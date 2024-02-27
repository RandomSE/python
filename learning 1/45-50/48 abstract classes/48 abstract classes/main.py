from abc import ABC, abstractmethod
# abstract classes: class containing one or more abstract methods
# abstract method: method containing a declaration but no implementation


class Vehicle(ABC):  # children classes must override this method
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
        return self

    def stop(self):
        print("This motorcycle is stopped")


class Car(Vehicle):
    def go(self):
        print("You drive the car")
        return self

    def stop(self):
        print("This car is stopped")


# vehicle = Vehicle()
motorcycle = Motorcycle()
car = Car()

motorcycle.go()
car.go()
motorcycle.stop()
car.stop()



