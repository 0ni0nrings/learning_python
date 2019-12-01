class Character:
    def __init__(self, name, age, power):
        self.name = name
        self.age = age
        self.power = power

character1 = Character('harry potter', 21, 'invisible')
character2 = Character('ron weasely', 19, 'cloak')
character3 = Character('hermoine', 19, 'wand')

print(character1.name)
print(character2.age)
print(character3.power)
