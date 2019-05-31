import random


class Product():

    def __init__(self, name=None, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        ratio = self.price / self.weight
        if ratio < 0.5:
            print('Not so stealable...')
        elif (ratio >= 0.5) and (ratio < 1):
            print('Kinda Stealable')
        else:
            print('Very stealable!')

    def explode(self):
        combust = self.flammability * self.weight
        if combust < 10:
            print('...fizzle.')
        elif (combust >= 10) and (combust < 50):
            print('...boom!')
        else:
            print('...BABOOM!!')


class BoxingGlove(Product):

    def __init__(self, name=None, price=10, weight=10,
                 flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        super().__init__(name=name, price=price, weight=weight,
                         flammability=flammability,
                         identifier=identifier)

    def punch(self):
        if self.weight < 5:
            print('That tickles.')
        elif (self.weight >= 5) and (self.weight < 15):
            print('Hey that hurt!')
        else:
            print('Ouch!')

    def explode(self):
        print('...its a glove.')
