class Animal(object):
    def __init__(self, animal_name, health):
        self.animal_name = animal_name
        self.health = health
        print self.animal_name

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_info(self):
        print "My name is {}, and I'm an unknown species; I'm some kind of animal".format(self.animal_name)
        print "Current health: {}".format(self.health)


animal1 = Animal("Apollo", 50)
animal1.walk().walk().walk().run().run().display_info()


class Dog(Animal):
    def __init__(self, animal_name):
        super(Dog, self).__init__(animal_name, 150)
        # self.health = 150

    def pet(self):
        self.health += 5
        return self

    def display_info(self):
        print "I'm {}, the dog".format(self.animal_name)
        super(Dog, self).display_info()


maja = Dog("Maja")
maja.walk().walk().walk().run().run().pet().pet().pet().pet().display_info()


class Dragon(Animal):
    def __init__(self, animal_name):
        super(Dragon, self).__init__(animal_name, 170)
        # self.health = 170

    def display_info(self):
        print "I'm {}, the scariest dragon in the land".format(self.animal_name)
        super(Dragon, self).display_info()

    def fly(self):
        self.health -= 10
        return self


oscarTheDragon = Dragon("Oscar")
oscarTheDragon.walk().fly().display_info()
