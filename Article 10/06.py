class Dog:
    dog_count = 0

    def __init__(self,name,breed,age):
        self.name = name    
        self.breed = breed  
        self.age = age
        Dog.dog_count += 1
        

tommy = Dog('tommy','Labrador Retriever',3)
print(Dog.dog_count)
dora = Dog('dora','German Shepherd',6)
print(Dog.dog_count)
luca = Dog('luca','Doberman',4)
print(Dog.dog_count)

