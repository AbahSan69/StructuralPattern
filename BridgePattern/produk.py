# product.py

class Product:
    def __init__(self, name, description, price, renderer):
        self.name = name
        self.description = description
        self.price = price
        self.renderer = renderer

    def display(self):
        return self.renderer.render(self)
