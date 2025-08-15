
class Dog:
    
    def __init__(self,name,breed,color,age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
        
    def dog_years_2_human_years(self):
        return self.age*7
        

    
tommy = Dog('Tommy','Labrador Retriever','Black',2)
print(tommy.dog_years_2_human_years())
