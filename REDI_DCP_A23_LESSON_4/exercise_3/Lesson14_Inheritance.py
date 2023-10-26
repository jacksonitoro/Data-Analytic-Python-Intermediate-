#Animal Classification task

class Animal:
    def __init__ (self, name, category, age):
        self.name = name
        self.category = category
        self.age = age

    def print_details(self):
        print(self.name, self.category, self.age, self.num_legs, self.num_fins )



class Mammal(Animal):
    def __init__(self, name, category, age, num_legs = 4, num_fins=0):
        super().__init__(name, category, age)
        self.num_legs = num_legs
        self.num_fins = num_fins

    
        

class Bird(Animal):
    def __init__(self, name, category, age, num_legs = 2, num_fins=0):
        super().__init__(name, category, age)
        self.num_legs = num_legs
        self.num_fins = num_fins
    
    

class Fish(Animal):
    def __init__(self, name, category, age, num_legs =0, num_fins=7):
        super().__init__(name, category, age)
        self.num_legs = num_legs
        self.num_fins = num_fins

     


#x = animal("Lion","carnivore", 10)
mammal = Mammal("Bambi", "Mammal", 3, 4)
bird = Bird("Igo", "Bird", 4, 2)
fish = Fish("Nemo", "Fish", 2,)
mammal.print_details()
bird.print_details()
fish.print_details()



