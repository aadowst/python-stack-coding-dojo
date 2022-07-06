class Ninja:
    def __init__ (self, first_name, last_name, treats=0, pet_food=0):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = {}
        self.treats = treats
        self.pet_food = pet_food
    
    def add_pet(self, name, type, tricks, health, energy):
        self.pet[name] = Pet(name, type, tricks, health, energy)
        return self

    def walk(self, name):
        self.pet[name].play()
        print("going for a walk")
        return self

    def feed(self, name):
        self.pet[name].eat()
        return self

    def bathe(self, name):
        self.pet[name].noise()
        return self

class Pet:
    def __init__ (self, name, type, tricks=0, health=10, energy=20):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self
    
    def play(self):
        print("a walk???")
        self.health += 5
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def noise(self):
        print("bark-meow!")
        return self

    def display_stats(self):
        print("Name:  ", self.name)
        print("Type:  ", self.type)
        print("Tricks:  ", self.tricks)
        print("Health:  ", self.health)
        print("Energy:  ", self.energy)
        return self

Adrian = Ninja("Adrian", "Dowst")

Adrian.add_pet("Sr. Fluffy", "mutt", 0, 10, 20) 
Adrian.add_pet("Sky Lobster", "what's a sky lobster?", 5, 15, 25) 
print(Adrian.pet["Sr. Fluffy"].health)

Adrian.walk("Sr. Fluffy")
Adrian.pet["Sr. Fluffy"].play()
Adrian.pet["Sr. Fluffy"].display_stats()
Adrian.bathe("Sky Lobster")
