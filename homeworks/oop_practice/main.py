import random
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age, money_availability, has_home):
        self.name = name
        self.age = age
        self.money_availability = money_availability
        self.has_home = has_home

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def make_money(self):
        pass

    def __repr__(self):
        return self.name


class Human(Person):
    def get_info(self):
        return f'Hi! My name is {self.name}, I"m {self.age} years old, I have {self.money_availability} and I live in ' \
               f'home = {self.has_home} '

    def make_money(self):
        self.money_availability += 1000
        return self.money_availability


class House(ABC):
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    @abstractmethod
    def apply_discount(self):
        pass

    def __repr__(self):
        return self.area

class Home(House):

    def apply_discount(self):
        self.cost *= 0.8
        return self.cost


class RealtorMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, houses, discount, buyers):
        self.name = name
        self.houses = houses
        self.discount = discount
        self.buyers = buyers

    def realtor_info(self):
        for i in range(len(self.houses)):
            print(f'''This is what I can offer:
                {self.houses[i].area} : {self.houses[i].cost}
                ''')

    def give_discount(self):
        for i in range(len(self.houses)):
            self.houses[i].cost -= self.discount
            print(f'''Prices with discounts:
              {self.houses[i].area} : {self.houses[i].cost}
              ''')

    def steal_money(self):
        for i in range(len(self.buyers)):
            if random.randint(1,10) == 2:
                self.buyers[i].money_availability *= 0.9
                print(f'stolen: {self.buyers[i].name} you now have {self.buyers[i].money_availability}')

alex = Human('Alex', 20, 1000, 'has home')
home1 = Home('Bibrka', 10000)
alex.make_money()
print(alex.get_info())
ira_realtor = Realtor('Irina', [home1], 1000, [alex])
(ira_realtor.realtor_info())
ira_realtor.steal_money()
ira_realtor.give_discount()

