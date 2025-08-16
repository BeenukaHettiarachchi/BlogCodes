class Dog:
    species = "Canis familiaris"  # <-- class-level data

    def __init__(self,name,breed,color,age):
        self.name = name    #     All of these
        self.breed = breed  #         are
        self.color = color  # <-- instance-level data
        self.age = age      # 
        
    def print_species(self):
        print(f'Species: {self.species}')
        
        
dora = Dog('Dora','German Shepherd','Black & Tan',6)
print(dora.species)
dora.print_species()