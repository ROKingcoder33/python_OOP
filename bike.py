# Create a new class called Bike
class Bike:

    # Give it attributes - price, max_speed, and miles
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    # add methods to the class
    def displayInfo(self):
        print(self.price, self.max_speed, self.miles)
        return self

    def ride(self):
        self.miles += 10
        print("Riding", self.miles)
        return self

    def reverse(self):
        self.miles -= 5
        print("Reversing", self.miles)
        return self


# Bike 1
bike1 = Bike(200, "25mph")
bike1.ride().ride().ride().reverse().displayInfo()

# Bike 2
bike2 = Bike(100, "10mph")
bike2.ride().ride().reverse().reverse().displayInfo()

# Bike 3
bike3 = Bike(150, "15mph")
bike3.reverse().reverse().reverse().displayInfo()
