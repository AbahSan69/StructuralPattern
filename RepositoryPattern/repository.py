# product_repository.py

from abc import ABC, abstractmethod
from produk import Produk

class ProductRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass
