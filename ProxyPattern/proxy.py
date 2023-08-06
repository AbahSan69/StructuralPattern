# proxy.py

from rekomendasi import Subject, RealSubject

class Proxy(Subject):
    def __init__(self):
        self.real_subject = RealSubject()

    def get_recommended_products(self):
        # Contoh validasi atau logika lain sebelum memanggil RealSubject
        # Misalnya, pastikan pengguna memiliki hak akses tertentu sebelum mendapatkan rekomendasi produk.
        has_permission = True # Lakukan validasi berdasarkan kebutuhan aplikasi Anda.

        if has_permission:
            return self.real_subject.get_recommended_products()
        else:
            return [] # Atau mungkin kembalikan pesan error jika tidak memenuhi persyaratan.
