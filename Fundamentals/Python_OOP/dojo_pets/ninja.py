import pet

class Ninja:
    def __init__ (self, first_name, last_name, treats=0, pet_food=0):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = {}
        self.treats = treats
        self.pet_food = pet_food
    
    def add_pet(self, name, type, tricks=0, health=10, energy=20):

        self.pet = {name: pet.Pet(name, type, tricks, health, energy)}
        return self

    def walk(self, name):
        self.pet[name].play()
        return self

    def feed(self, name):
        self.pet[name].eat()
        return self

    def bathe(self, name):
        self.pet[name].noise()
        return self

Adrian = Ninja("Adrian", "Dowst")
print(Adrian.first_name)

Adrian.add_pet("Sr. Fluffy", "mutt")
Adrian.add_pet("Shark", "basset hound")
# shark = pet.Pet("Shark", "basset hound")
print(Adrian.pet["Sr. Fluffy"].name)
# print(shark.name)
# print(type(shark))

# Adrian.walk("Sr. Fluffy")
# Adrian.bathe("Sr. Fluffy")