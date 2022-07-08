# import ninja
class Pet:
    def __init__ (self, name, type, tricks=0, health=20, energy=30):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self
    
    def play(self):
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

# Adrian = ninja.Ninja("Adrian", "Dowst")
# print(Adrian.last_name)



# ninja.Adrian.add_pet("Sr. Fluffy", "mutt", 0, 10, 20)
# print(Adrian.pet["Sr. Fluffy"].name)

# Adrian.walk("Sr. Fluffy")
# Adrian.bathe("Sr. Fluffy")