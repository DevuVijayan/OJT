import re

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age if isinstance(age, int) and age > 0 else None
        self.email = email if re.match(r"[^@]+@[^@]+\.[^@]+", email) else None

person1 = Person("Devu", 25, "devu@devuvi.com")
person2 = Person("lisy", 30, "lisy@lisyjayakumar")
person3 = Person("Riya", 35, "riya@riyaroy.com")

print(person1.name, person1.age, person1.email) 
print(person2.name, person2.age, person2.email)
print(person3.name, person3.age, person3.email)
