class Car:
    # the __init__ method with attributes:
    # price, speed, fuel, mileage
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    # methods needed for this project

    def display_all(self):
        print("Price: " + str(self.price))
        print("Speed: " + str(self.speed))
        print("Fuel: " + str(self.fuel))
        print("Mileage: " + str(self.mileage))
        print("Tax: " + str(self.tax))
        print("---" * 10)
        print("\n\n")


car1 = Car(2000, "35mph", "Full", "15mph")
car1.display_all()

car2 = Car(2000, "5mph", "Not Full", "105mph")
car2.display_all()

car3 = Car(5000, "15mph", "Somewhat Full", "45mph")
car3.display_all()

car4 = Car(10000, "45mph", "Almost Empty", "35mph")
car4.display_all()

car5 = Car(10001, "75mph", "Empty", "85mph")
car5.display_all()

car6 = Car(20000, "35mph", "Full", "30mph")
car6.display_all()
