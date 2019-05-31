import random
from acme import Product

class Report(Product):
    ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 
            'Improved']
    NOUN = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

    def __init__(self, name=None, price=random.randint(5,100), 
                 weight=random.randint(5,100),
                 flammability=random.uniform(0,2.5), 
                 identifier=random.randint(1000000,9999999),
                 inventory=30):
        super().__init__(name=name, price=random.randint(5,100),                      weight=random.randint(5,100),
                         flammability=random.uniform(0,2.5),
                         identifier=random.randint(1000000,9999999),)
        self.inventory = inventory

    def generate_products(self):
        self.inventory = random.randint(1, 30)
        prod_list = [random.sample(ADJECTIVES, 1) 
                     + random.sample(NOUN, 1) 
                     for i in range(self.inventory+1)]
        prod_list = [' '.join(i) for i in prod_list]
        return [Report(i) for i in prod_list]
    
    def inventory_report(self):
        inventory = generate_products()
        price = [product.price for product in inventory]
        weight = [product.weight for product in inventory]
        flame = [product.flammability for product in inventory]
        print('Unique product names:', len(inventory))
        print('Avg price:', sum(price)/len(inventory))
        print('Ave weight:', sum(weight)/len(inventory))
        print('Avg flame:', sum(flame)/len(inventory))

if __name__ == '__main__':
    inventory_report(generate_products())