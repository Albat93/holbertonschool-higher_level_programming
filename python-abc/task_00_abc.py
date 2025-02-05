#!/usr/bin/python3
"""creating a class animal with subaclasses
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """create a class animal
    """

    @abstractmethod
    def sound(self):
        """abstract method that is meant to return sound of specific animal"""
        pass


class Dog(Animal):
    """create a subclass dog that inherit the class animal
    """

    def sound(self):
        """return the sound made by a dog"""
        return "Bark"


class Cat(Animal):
    """create a subclass cat that inherit the class animal
    """

    def sound(self):
        """return the sound made by a cat"""
        return "Meow"
