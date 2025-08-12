
class Dog:
    
    def __init__(self,name,breed,color,age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
        
        
    @classmethod
    def from_str(cls,args):
        name, breed, color, age = args.split(',')
        return cls(name,breed,color,int(age))
    

d = Dog.from_str('Luca,Doberman,Black & Rust,4')
print(d.name)