# pets.py

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def display(self):
        message = f"{self.name} is a {self.species}"
        print(message)


mr_meow = Pet("alice", "cat")

mr_meow.display()