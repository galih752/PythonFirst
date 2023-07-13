#membuat penampung
table = {}
#Menambah data
table[1] = "Avanza"
table[2] = "Toyota"
table[3] = "Suzuki"
table[4] = "Honda Brio"
table[5] = "Hyundai"

#Menampilkan Menu
def etalase():
    print("Etalase :")
    print(" 1.",table[1],"\n","2.",table[2],"\n","3.",table[3],"\n","4.",table[4],"\n","5.",table[5])

    # Memilih tipe mmobil yang diinginkan
    print()
    print("Silahkan pilih mobil kesukaan")
    print()
    buy = int(input("Masukkan pilihan :"))
    if buy == 1:
        print("Pilihan anda mobil ",table[1])
        etalase()
    elif buy == 2:
        print("Pilihan anda mobil ",table[2])
        etalase()
    elif buy == 3:
        print("Pilihan anda mobil ",table[3])
        etalase()
    elif buy == 4:
        print("Pilihan anda mobil ", table[4])
        etalase()
    elif buy == 5:
        print("Pilihan anda mobil ", table[5])
        etalase()
    else:
        print("Pilihan anda tidak tersedia!")
etalase()