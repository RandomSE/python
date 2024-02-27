from animals import Rabbit, Fish, Hawk, Moose


class Car:
    # class variables
    wheels = 4
    driving = False
    current_velocity = 0  # kph  # (the 4 could be changed to another value if you want the car to win more.)
    strength = current_velocity * 10

    def __init__(self, make, model, year, colour):  # instance variable
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.update_strength()

    def update_strength(self):
        self.strength = self.current_velocity * 10

    def fight(self, animal):
        print(f"{self.make} {self.model} is fighting {animal.name}")
        if self.strength > animal.strength:
            print(f"{self.make} {self.model} wins!")
            animal.alive = False
        elif self.strength < animal.strength:
            print(f"{animal.name} wins!")
            self.driving = False
            print(f"The {self.make} {self.model} crashed into {animal.name}. The engine stopped.")
        else:
            print("It's a draw!")

    def tostring(self):  # basic info for other methods
        return (str(self.make) + " " + str(self.model) + " " + str(self.year) + " " + str(self.colour) +
                " is moving at:  " + str(self.current_velocity) + " KPH")

    def start_engine(self):
        if not self.driving:
            self.driving = True
            print(self.tostring() + " engine started.")
        else:
            print("The engine has already been started.")

    def stop_engine(self):
        if self.driving:
            self.driving = False
            print(self.tostring() + " engine stopped.")
            if self.current_velocity > 0:
                print("That was not a good idea. You cannot steer or brake. crash imminent.")  # running over animals
        else:
            print("The engine has not been started yet.")

    def accelerate(self):
        if self.driving:
            self.current_velocity += 20  # not realistic as it would take time
            self.update_strength()
            return self.tostring() + " is accelerating.   Current speed:" + str(self.current_velocity)
        else:
            return self.tostring() + " cannot accelerate, you need to start the engine first.."

    def brake(self):  # basically accelerate but in the opposite direction
        if self.driving and self.current_velocity > 0:
            self.current_velocity -= 20  # not realistic as it would take time
            self.update_strength()
            return self.tostring() + " is braking.   Current speed:" + str(self.current_velocity)
        elif not self.driving:
            return self.tostring() + " cannot brake, you need to start the engine first.."
        elif self.current_velocity <= 0:
            return self.tostring() + " is not moving."


def car_interface(car):
    while True:
        print("\n=== Car Interface ===")
        print("0. Information on current car")
        print("1. Start Engine")
        print("2. Stop Engine")
        print("3. Accelerate")
        print("4. Brake")
        print("5. Fight Animal")
        print("6. Exit")

        choice = input("Enter your choice (0-6): ").strip()

        if choice == "0":
            print(car.tostring())
        elif choice == '1':
            car.start_engine()
        elif choice == '2':
            car.stop_engine()
        elif choice == '3':
            print(car.accelerate())
        elif choice == '4':
            print(car.brake())
        elif choice == '5':
            animal_choice = input("Enter the name of the animal to fight: ").strip()
            rabbit_instance = Rabbit("Mr carrot")
            fish_instance = Fish("Cape Cod")
            hawk_instance = Hawk("Dennis the menace")
            moose_instance = Moose("Heavyweight champion")

            if animal_choice.lower().strip() == "rabbit":
                car.fight(rabbit_instance)
            elif animal_choice.lower().strip() == "fish":
                car.fight(fish_instance)
            elif animal_choice.lower().strip() == "hawk":
                car.fight(hawk_instance)
            elif animal_choice.lower().strip() == "moose":
                car.fight(moose_instance)
            else:
                print("Invalid animal choice.")
        elif choice == '6':
            print("Exiting Car Interface. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 6.")
