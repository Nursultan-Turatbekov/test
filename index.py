# Наследование
class Good:
    is_sold = False
  

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Computer(Good):
    hdd = 1000
    windows = True

    def __init__(self, price, model):
        name = f"Computer {model}"
        super().__init__(name=name, price=price)    

# Инкапсуляция
class A:
    def _private(self):
        print("Private method")

# Полиморфизм   
class Car:
    def nothing(self):
        pass

class BMW:
    def nothing(self, word):
        print(word + "!")

#Абстракция
from abc import ABC, abstractmethod

class B(ABC):
    @abstractmethod
    def hello(self):
        print("hello")

class Ad(B):
    def hello(self):
        super().hello()
        print("Hi")        