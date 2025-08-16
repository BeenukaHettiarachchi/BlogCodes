class Dog:
    species = ""

    def __init__(self,name,breed,color,age):
        self.name = name    
        self.breed = breed  
        self.age = age      
        
    @classmethod
    def set_species(cls,species):
        cls.species = species

print(Dog.species)
Dog.set_species('Canis familiaris')
print(Dog.species)