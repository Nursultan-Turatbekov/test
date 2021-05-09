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