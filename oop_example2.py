class Character:
    club = "fightclub" # global class variable
    def __init__(self, name, age):
        self.name = name # attribute/properties
        self.age = age
        

    def hand_attack(self): # method
        return 'punch'
    
    def leg_attack(self):
        return 'kick'
    
fighter1 = Character('taylor', 21) # instantiate
fighter2 = Character('durden', 22)
print(fighter1.name)
print(fighter2.name)
print(fighter1.hand_attack())
print(fighter2.leg_attack())
print(fighter1.club)
print(fighter2.club)


    


