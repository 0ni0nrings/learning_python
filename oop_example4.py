class Animal:
    def __init__(self):
        print('I am animal')

    def talk(self):
        print('I can speak in my own language')
    
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print(" I am a dog")
    
class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("I am a cat")

mydog = Dog()
mycat = Cat()
print(mycat.talk())
print(mydog.talk())
