class Node:
    def __init__(self,isi):
        self.raight = None
        self.left = None
        self.data = isi
    def tambah(self,isi):
        if isi < self.data:
            if isi < self.data:
                self.left = Node(isi)
            else:
                self.left.tambah(isi)
        elif isi > self.data:
            if self.raight is None:
                self.raight = Node(isi)
            else:
                self.raight.tambah(isi)
        else:
            self.data = isi
    def tampilkan(self):
        if self.left:
            self.left.tampilkan()
        print(self.data)
        if self.raight:
            self.raight.tampilkan()




hasil = Node (10)
hasil.tambah(5)
hasil.tambah(70)
hasil.tambah(30)

hasil.tampilkan()