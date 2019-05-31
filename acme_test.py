#!/usr/bin/env python
import unittest
from acme import Product
from acme_report import Report


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_weight(self):
        weight = Product('Test Weight')
        self.assertEqual(weight.weight, 20)

    def test_default_inventory(self):
        report = Report('Test Inventory')
        self.assertEqual(report.inventory, 30)


if __name__ == '__main__':
    unittest.main()


# Code reviews help catches our mistake and helps us improve on them.  We take in constructive criticism and grow together.

# Using containers is like have a mini version of a Virtual Machine. The difference is that it is faster and we can set-up the OS whereas the VM is a copy of the OS. Also having a container is good for testing out code since the environment will always be the same compared to the orginal OS where we might change the environment periodically.