#The interface segregation principle states that an interface should be as small a possible in terms of cohesion. 
#In other words, it should do ONE thing.
'''
Code not following Principle:

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def fly(self):
        pass
'''
from abc import ABC, abstractmethod

class Movable(ABC):
    @abstractmethod
    def go(self):
        pass


class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass

class Aircraft(Flyable):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")

class Car(Movable):
    def go(self):
        print("Going")