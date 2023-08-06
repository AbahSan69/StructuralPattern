# main.py

from produk_factory import ProductFactory

def main():
    product_factory = ProductFactory()

    # Dapatkan produk dari factory (jika sudah ada, akan digunakan kembali)
    product1 = product_factory.get_product("Ventela", "Ini Adalah Sepatu Ventela", 100000)
    product2 = product_factory.get_product("NB", "Ini Adalah Sepatu NB", 150000)

    # Cek apakah produk1 dan produk2 menggunakan objek yang sama
    print(product1 is product2)  # True, karena menggunakan objek yang sama

    # Dapatkan produk lagi dengan data yang sama
    product3 = product_factory.get_product("Ventela", "Ini Adalah Sepatu Ventela", 100000)

    # Cek apakah produk1 dan produk3 menggunakan objek yang sama
    print(product1 is product3)  # True, karena menggunakan objek yang sama

if __name__ == "__main__":
    main()
