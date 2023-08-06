# product_repository_impl.py

from repository import ProductRepository
from produk import Produk

class ProductRepositoryImpl(ProductRepository):
    def __init__(self):
        self.products = [
            Produk(1, 'Ventela', 'Produk Sepatu Ventela', 100000),
            Produk(2, 'NB', 'Produk Sepatu New Balance', 150000),
            Produk(3, 'Jhonson', 'Produk Sepatu Jhonson', 200000),
            # Tambahkan lebih banyak data produk di sini
        ]

    def get_all(self):
        return self.products

    def get_by_id(self, id):
        return next((product for product in self.products if product.id == id), None)
