# renderer.py

from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render(self, product):
        pass

class TextRenderer(Renderer):
    def render(self, product):
        return f"{product.name} - {product.description} - {product.price}"
