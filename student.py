class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self) -> str:
        return f"{self.name} is {self.age} years old"