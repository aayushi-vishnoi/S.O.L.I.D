# Open Closed Principle: 
#It states that a class, method, and function should be open for extension but closed for modification.

'''
Code not following OCP

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'


class PersonStorage:
    def save_to_database(self, person):
        print(f'Save the {person} to database')

    def save_to_json(self, person):
        print(f'Save the {person} to a JSON file')


if __name__ == '__main__':
    person = Person('John Doe')
    storage = PersonStorage()
    storage.save_to_database(person)

'''
from abc import abstractclassmethod, ABC

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'


class PersonStorage(ABC):
    @abstractclassmethod
    def save(self,person):
        pass

class PersonDB(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to database')


class PersonJSON(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a JSON file')

class PersonXML(PersonStorage):
     def save(self, person):
        print(f'Save the {person} to a XML file')

if __name__ == '__main__':
    person = Person('John Doe')
    storage = PersonXML()
    storage.save(person)