# main.py

from implemen_repository import ProductRepositoryImpl

def main():
    product_repository = ProductRepositoryImpl()

    # Mengambil semua produk
    products = product_repository.get_all()
    for product in products:
        print(f'{product.nama} - {product.deskripsi} - {product.harga}')

    # Mengambil produk berdasarkan ID
    product_id = 2
    product = product_repository.get_by_id(product_id)
    if product:
        print(f'Produk dengan ID {product_id}: {product.nama} - {product.deskripsi} - {product.harga}')
    else:
        print(f'Produk dengan ID {product_id} tidak ditemukan.')

if __name__ == "__main__":
    main()
