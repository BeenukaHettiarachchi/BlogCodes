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
        
    def eat(self, what):
        what = 'a '+what if what[0].lower() not in ['a','e','i','o','u'] else 'an '+what
        print(self.name, 'is eating',what)


tommy = Dog('tommy','Labrador Retriever','Black',3)
dora = Dog('dora','German Shepherd','Black & Tan',6)
luca = Dog('luca','Doberman','Black & Rust',4)

tommy.eat()
dora.sleep()
luca.run()