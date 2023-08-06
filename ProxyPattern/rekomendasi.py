# recommendation.py

from abc import ABC, abstractmethod
from produk import Produk

class Subject(ABC):
    @abstractmethod
    def get_recommended_products(self):
        pass

class RealSubject(Subject):
    def get_recommended_products(self):
        # Lakukan logika rekomendasi produk di sini
        # Misalnya, rekomendasikan produk berdasarkan preferensi pengguna, kategori, atau popularitas.
        products = [
            Produk(1, 'Ventela', 'Produk Sepatu Ventela', 100000),
            Produk(2, 'NB', 'Produk Sepatu New Balance', 150000),
            Produk(3, 'Jhonson', 'Produk Sepatu Jhonson', 200000),
            # Tambahkan lebih banyak data produk di sini
        ]
        return products
