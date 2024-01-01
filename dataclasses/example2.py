from dataclasses import dataclass, field


# order=True specifies that they can be ordered 
# frozen=False specifies that the attributes can be changed/updated else if True, it means that the data cannot be changed anywhere in the code 

# sort_index: int = field(init=False, repr=False) used to specify sorting, init False = doesn't have to be initialise,
# repr=False : specifies that it should not be printed when object is printed 

#  for fields you dont want to initialize : 'field(init=False, repr=False)'

@dataclass(order=True,frozen=False)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    # default value
    strength: int = 100

    def __post_init__(self):
        # called after the values have been set 
        # we can: self.sort_index = self.strength  buut if frozen= true that wont work so instead use object.__setattr__
        object.__setattr__(self, 'sort_index', self.strength)

    def __str__(self):
        return f'{self.name}, {self.job} ({self.age})'


person1 = Person("Geralt", "Witcher", 30, 99)
person2 = Person("Yennefer", "Sorceress", 25)
person3 = Person("Yennefer", "Sorceress", 25)

print(person1)
print(person2)
print(id(person2))
print(id(person3))
print(person3 == person2)
print(person1 > person2)


