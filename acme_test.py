#!/usr/bin/env python
import unittest
from acme import Product
from acme_report import generate_products, inventory_report
from acme_report import ADJECTIVES, NOUN


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_weight(self):
        prod = Product('Test Weight')
        self.assertEqual(prod.weight, 20)

    def test_default_flammability(self):
        prod = Product('Test Flammability')
        self.assertEqual(prod.flammability, 0.5)


class AcmeReportTest(unittest.TestCase):
    """Making sure Acme Report is correct"""
    def test_default_inventory(self):
        self.assertEqual(len(generate_products()), 30)

    # List of name from generated products
    name = [name.name for name in generate_products()]

    # Makes a list of sublist and add a comma
    # to empty spaces
    name = [i.split() for i in name]

    # Create flat_list to test for all individual
    flat_list = []

    # Loop to break-up sublist and append all words
    for sublist in name:
        for word in sublist:
            flat_list.append(word)

    def test_legal_names(self, flat_list=flat_list):
        for i in (ADJECTIVES + NOUN):
            self.assertIn(i, flat_list)


if __name__ == '__main__':
    unittest.main()

# Code reviews help catches our mistake and helps us improve on them.  We take
# in constructive criticism and grow together.

# Using containers is like have a mini version of a Virtual Machine. The
# difference is that it is faster and we can set-up the OS whereas the VM is a
# copy of the OS. Also having a container is good for testing out code since
# the environment will always be the same compared to the orginal OS where we
# might change the environment periodically.
