from abc import ABC, abstractmethod


class Object(ABC):
    def __init__(self, size):
        self.__size = size

    @abstractmethod
    def shape(self):
        pass

    def get_size(self):
        return self.__size


class Phone(Object):
    def shape(self):
        print("This device is: ", self.get_size())


class Comp(Object):
    def shape(self):
        print("This device is: ", self.get_size())


Phone_size = input("What do you have?: ")
Comp_size = input("What do you have?: ")


Object = [Phone(Phone_size), Comp(Comp_size)]


for O in Object:
    O.shape()
