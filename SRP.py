'''The single responsibility principle (SRP) states that every class, method, 
and function should have only one job or one reason to change.'''

''' 
The below code not follwing SRP.

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'

    @classmethod
    def save(cls, person):
        print(f'Save the {person} to the database')


if __name__ == '__main__':
    p = Person('John Doe')
    Person.save(p)

'''
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'

class PersonDB:
    def save(self,person):
        print(f'Save the {person} to the database')

p = Person("John")
db = PersonDB()
db.save(p)