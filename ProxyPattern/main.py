# main.py

from proxy import Proxy

def main():
    proxy = Proxy()
    recommended_products = proxy.get_recommended_products()

    print("Recommended Products:")
    for product in recommended_products:
        print(f'{product.nama} - {product.deskripsi} - {product.harga}')

if __name__ == "__main__":
    main()
