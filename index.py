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

#Генератор   
def simple_generator(val):
   while val > 0:
       val -= 1
       yield 1

gen_iter = simple_generator(5)

# Метоклассы
def my_metaclass(class_name, parents, attributes):
    print('In metaclass, creating the class.')
    return type(class_name, parents, attributes)


def my_class_decorator(class_):
    print('In decorator, chance to modify the claqss.')
    return class_


@my_class_decorator
class C(metaclass=my_metaclass):
    def __init__(self):
        print('Creating object.')

#Экземпляр класса
class Student:
    def __init__(self, name, age, major, gpa):
    self.name = name
    self.age = age
    self.major = major
    self.gpa = gpa    