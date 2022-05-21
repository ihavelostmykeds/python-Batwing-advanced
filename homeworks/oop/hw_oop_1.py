class Animals:
    def eat(self):
        print('yum')

    def sleep(self):
        print('Zzzz')


class Raindeer(Animals):
    def fight(self):
        print('Hiya!')


class Horse(Animals):
    def neigh(self):
        print('Neeeeeigh!')


class Chicken(Animals):
    def fly(self):
        print('I am flying!')


class Cockroach(Animals):
    def run(self):
        print('woah!')


class Dog(Animals):
    def bark(self):
        print('woof!')


class Human:
    def eat(self):
        print('yum!')

    def sleep(self):
        print('ZZZZzzzz')

    def study(self):
        print('going to school!')

    def work(self):
        print('going to work!')


class Centaur(Horse, Human):
    def attack(self):
        print('attacking!')


small_deer = Raindeer()
small_deer.fight()
horse = Horse()
horse.neigh()
chicken = Chicken()
chicken.fly()
roach = Cockroach()
roach.run()
puppy = Dog()
puppy.bark()
centaur = Centaur()
centaur.neigh()
centaur.eat()
centaur.sleep()
centaur.work()
centaur.study()
centaur.attack()

print(f'is my small_deer an instance of Raindeer? {isinstance(small_deer, Raindeer)}')
print(f'is my horse an instance of Horse? {isinstance(horse, Horse)}')
print(f'is my chicken an instance of Chicken? {isinstance(chicken, Chicken)}')
print(f'is my roach an instance of Cockroach? {isinstance(roach, Cockroach)}')
print(f'is my puppy an instance of Dog? {isinstance(puppy, Dog)}')



