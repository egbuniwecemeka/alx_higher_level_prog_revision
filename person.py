class Person:
    def __init__(self, name, age):
        """ Initializing instance attributes
            Attributes:
            name(str): ...
            age(int): ...
        """
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"My name is {self.name}, and I am {self.age} years old"
        
    def __repr__(self):
        return f"{type(self).__name__}(name:{self.name}, age:{self.age})"