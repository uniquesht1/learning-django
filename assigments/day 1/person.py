class Person:
    def __init__(self, name, age, address):
        print("I am a person")
        self.name = name
        self.age = age
        self.address = address

    def start(self):
        print("My name is",self.name,)
        print("I am", self.age ,"years old")
        print("I live in",self.address,)
        


class Male(Person):
    def start(self):
        super().start()
        print("I can eat,walk and run.\n")

class Female(Person):
    def start(self):
        super().start()
        print("I can eat,walk and run")

ram = Male(name="Ram", age=27, address="Ayodhya")
ram.start()

sita = Female(name="Sita", age=25, address="Janakpur")
sita.start()
