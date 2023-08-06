# product.py

class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def display(self):
        return f"{self.name} - {self.description} - {self.price}"
