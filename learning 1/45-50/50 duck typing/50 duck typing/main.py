# duck typing: concept where the class of an object is less important than the methods
# class type not checked if minimum methods/attributes are met: "if it walks and quacks like a duck, is duck"

class Duck:
    def talk(self):
        print("it quacks")
        return self

    def walk(self):
        print("it walks")
        return self


class Chicken:
    def talk(self):
        print("it clucks")
        return self

    def walk(self):
        print("it waddles")
        return self


class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the thing")
        return self


chicken = Chicken()
duck_1 = Duck()
person = Person()

# person.catch(duck_1)
person.catch(chicken)  # both chicken and duck share walk and talk, so can be used.
