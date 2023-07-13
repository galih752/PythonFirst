class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun
    def info(self):
        print("Merk:", self.merk)
        print("Tahun:", self.tahun)
    def __str__(self):
        return f"{self.merk} ({self.tahun})"
class Mobil(Kendaraan):
    def __init__(self, merk, tahun, warna):
        super().__init__(merk, tahun)
        self.warna = warna
    def info_mobil(self):
        self.info()
        print("Warna:", self.warna)
    def __str__(self):
        return f"Mobil {self.merk} ({self.tahun}) - {self.warna}"
merek = input("Masukkan merk :")
tahunnya = int(input("Masukkan Tahun Produksi :"))
warnanya = input("Masukkan warna yang diinginkan :")
# Membuat objek dari kelas Mobil
mobil1 = Mobil(merek, tahunnya, warnanya)
# Menggunakan method dari superclass Kendaraan
print(str(mobil1))