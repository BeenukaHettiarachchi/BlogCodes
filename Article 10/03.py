
class Dog:
    
    def __init__(self,name,breed,color,age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
        
        
    @classmethod
    def from_str(cls,the_str):
        name, breed, color, age = the_str.split(',')
        return cls(name,breed,color,int(age))
    
    @classmethod
    def from_list(cls,the_list):
        name, breed, color, age = the_list
        return cls(name, breed, color, age)
    
    @classmethod
    def puppy(cls,name,breed,color):
        return cls(name,breed,color,0)
    
    


dora = ['Dora','German Shepherd','Black & Tan',6]
    

dog_1 = Dog.from_str('Luca,Doberman,Black & Rust,4')
dog_2 = Dog.from_list(dora)
print(dog_2.name)


rex = Dog.puppy('Rex','German Shepherd','Black & Tan')
print(rex.age)