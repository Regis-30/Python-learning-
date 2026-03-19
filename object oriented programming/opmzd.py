from abc import ABC, abstractmethod


# ---------- ABSTRACTION ----------
class Animal(ABC):

    def __init__(self, sound):
        self.__sound = sound   # encapsulation

    @abstractmethod
    def voice(self):
        pass

    def get_sound(self):
        return self.__sound


# ---------- INHERITANCE ----------
class Dog(Animal):

    def __init__(self):
        super().__init__("barking")

    def voice(self):
        print("This animal is", self.get_sound())


class Cat(Animal):

    def __init__(self):
        super().__init__("meowing")

    def voice(self):
        print("This animal is", self.get_sound())


# ---------- FACTORY ----------
animal_factory = {
    "dog": Dog,
    "cat": Cat
}


# ---------- USER INPUT ----------
choice = input("What animal is this (dog/cat): ").lower()


# ---------- OBJECT CREATION + POLYMORPHISM ----------
animal = animal_factory.get(choice)

if animal is None:
    print("SORRY, Animal not detected")
else:
    animal().voice()
