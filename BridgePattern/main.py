# main.py

from produk import Product
from render import TextRenderer

def main():
    product = Product("Ventela", "Ini Adalah Produk Sepatu Ventela", 100000, TextRenderer())
    result = product.display()
    print(result)

if __name__ == "__main__":
    main()
