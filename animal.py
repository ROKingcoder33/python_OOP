class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print(self.name + " final health score is " + str(self.health))
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self


animal1 = Animal("Sparky")
animal1.walk().walk().walk().run().run().displayHealth()

dog1 = Dog("Rover")
dog1.walk().walk().walk().run().run().pet().displayHealth()

dragon1 = Dragon("Fire Ball")
dragon1.walk().walk().run().run().fly().fly().displayHealth()