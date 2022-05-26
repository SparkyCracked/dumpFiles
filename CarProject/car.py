class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = input("Enter color of car: ")

    def drive(self):
        print("The " + self.model + " " + self.make + " car is driving")

    def stop(self):
        print("The " + self.make + " " + self.model + " is now stopped")

    def turnL(self):
        print("The " + self.model + " " + self.make + " car has turned left")

    def turnR(self):
        print("The " + self.make + " " + self.model + " has turned right")

    def infoOnCar(self):
        print("The make of the car: " + self.make)
        print("The model of the car: " + self.model)
        print("The year the car was released: " + str(self.year))
        print("The colour of the car: " + self.color)
