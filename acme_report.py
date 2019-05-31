import random
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUN = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


class Report(Product):

    # __init__(# Use default numbers from Product)
    def __init__(self, name=None, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        # Change the default parameters
        super().__init__(name=name, price=random.randint(5, 100),
                         weight=random.randint(5, 100),
                         flammability=random.uniform(0, 2.5),
                         identifier=random.randint(1000000, 9999999))


def generate_products(inventory=30):

    prod_list = [random.sample(ADJECTIVES, 1) + random.sample(NOUN, 1)
                 for i in range(inventory)]
    prod_list = [' '.join(i) for i in prod_list]
    return [Report(i) for i in prod_list]


def inventory_report(products):
    # Extract price, weight and flame from products
    price = [product.price for product in products]
    weight = [product.weight for product in products]
    flame = [product.flammability for product in products]
    # Print
    print('Unique product names:', len(products))
    print('Avg price:', sum(price)/len(products))
    print('Ave weight:', sum(weight)/len(products))
    print('Avg flame:', sum(flame)/len(products))

if __name__ == '__main__':
    inventory_report(generate_products())
