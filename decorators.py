def dekoratorku(func):
    def isi_dec(*args, **kwargs):
        print("Sebelum function")
        isi = func()
        print("Ini setelah function")
        return isi
    return isi_dec

@dekoratorku
def teks():
    print("Galih")

@dekoratorku
def teks2():
    print("Ahmad")

print(teks2())