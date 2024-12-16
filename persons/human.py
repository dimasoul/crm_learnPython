class Human:
    MAX_AGE = None
    MIN_AGE = None
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)
