
class Dog:
    
    def __init__(self,name,breed,color,age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
    
    @staticmethod
    def dog_years_2_human_years(dog_years):
        return dog_years*7
    
    def age_in_human_years(self):
        return self.dog_years_2_human_years(self.age)
        

# Without creating an instance
human_years = Dog.dog_years_2_human_years(3)
print(human_years)
    
# With creating an instance
tommy = Dog('Tommy','Labrador Retriever','Black',2)
human_years = tommy.dog_years_2_human_years(2)
print(human_years)

dora = Dog('Dora','German Shepherd','Black & Tan',6)
print(dora.age_in_human_years())