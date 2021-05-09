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

#Композиция 
class Salary:
    def __init__(self,pay):
        self.pay = pay

    def getTotal(self):
        return (self.pay*12)

class Employee:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = Salary(self.pay)

    def annualSalary(self):
        return "Total: " + str(self.salary.getTotal() + self.bonus)

#Итератор

class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration