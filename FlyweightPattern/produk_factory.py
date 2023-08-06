# product_factory.py

from produk import Product

class ProductFactory:
    def __init__(self):
        self.products = {}

    def get_product(self, name, description, price):
        key = f"{name}-{description}-{price}"
        if key not in self.products:
            self.products[key] = Product(name, description, price)
        return self.products[key]
