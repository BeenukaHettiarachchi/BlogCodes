class Dog:
    
    def __init__(self,name,breed,color,age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
        
    def run(self):
        print(self.name, 'is running.')
        
    def sleep(self,):
        print(self.name,'is sleeping.')
        
    def eat(self):
        print(self.name, 'is eating.')
        
    def eat_sleep(self):
        self.eat()
        self.sleep()


tommy = Dog('tommy','Labrador Retriever','Black',3)
dora = Dog('dora','German Shepherd','Black & Tan',6)
luca = Dog('luca','Doberman','Black & Rust',4)


dora.eat_sleep()