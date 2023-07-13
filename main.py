# import array as arr
# #Basic Syntax
# #Menampilkan Tulisan Hello World!
# print("Hello World!")

# #String
# str = "Nama saya Galih.."
# print (str)
#
# #integer
# int = 12
# print(int)
#
# #float
# float = 20.5
# print(float)
#
# #boolean
# bool = False
# print(bool)
#
# #Kondisi
# anka = int(input("Masukkan nilai anda : "))
#
# #if condition
# if angka == 10:
#     print("Nilai kamu 10")
#
# #Else If / Elif condition
# elif angka == 8:
#     print("Nilai Kamu bukan 10 tapi 8")
#
# #Else
# else:
#     print("Nilai anda tidak sesuai!")
#
# #Casting type
#
# #String ke Integer
# str = "100"
# result_int = int(str)
# print(result_int,' dengan tipe ',type(result_int))
#
# #integer ke float
# nilai_int = 150
# result_float = float(nilai_int)
# print(result_float, ' Memiliki tipe data ',type(result_float))
#
# # integer ke boolean
# nilai = 1000 #True karena bernilai, jika nol (0) maka akan False
# bool = bool(nilai)
# print(bool, ' bertipe data ', type(bool))
#
# #Exception
# try:
#     nilai = 100 * lima
#     print(nilai)
# except:
#     print("Terjadi kesalahan")
#
# #Function
# def myName():
#     nama = "Nama saya RD.Galih Rakasiwi"
#     print (nama)
# myName()
#
# #Built in Function
# def penjumlahan(a,b):
#     return a + b
#
# hasil = penjumlahan(100,200)
# print(hasil)
#
# #Tuple
# point = (10,20,30,40)
#
# # menampilkan point ke 2 yaitu 30
# print(point[2])
#
# #Menampilkan semua
# employe = ('Galih',17,'Back End')
#
# # menampilkan tuple employe
# print(' Nama : ',employe[0],'\n','Umur : ',employe[1],'\n','Devisi : ',employe[2])
#
# #Set
# student = {'Asep','Ahmad','Saeful'}
#
# #menampilkan hasil True
# print('Asep'in student)
#
# #menampilkan hasil False
# print(('asep' in student))
#
# # memisahkan string dan menghilangkan duplikat tapi tidak berurutan
# char = set("Balloon")
# print(char)
#
# #Dictionari
# dict = {
#     'Nama ': 'Asep',
#     'Alamat ': 'Bandung',
#     'Umur ' : 22,
#     'Hobi ' : 'Renang'
# }
#
# #Mengubah umur menjadi 30
# dict['Umur '] = 30
#
# #Menampilkan hasil yang telah dirubah
# print(' Nama : ',dict['Nama '],'\n',
#       'Alamat : ',dict['Alamat '],'\n',
#       'Umur : ',dict['Umur '],'\n',
#       'Hobi :',dict['Hobi '])
#
# #Perulangan
#
# #Ingin melakukan perulangan hingga 10
# for x in range(1,11):
#     #mencari angka yang sisa baginya tidak sama dengan nol
#     if x % 2 != 0:
#         # untuk menampilkan angaka ganjil tersebut
#         print(x)
#
# #Array
# angka = arr.array('i',[1,2,3,4,5,6,7,8,9]) #integer
# print(angka[5])
#
# Huruf = ['Asep', 'Abeh', 'Ahmad']
# print(Huruf[2])
#
# campur = ['Gaalih',15,'Asep',20]
# print(campur[2])
#

# #membuat penampung
# table = {}
#
# #Menambah data
# table["Mobil"] = 1
# table["Motor"] = 2
# table["Tas"] = 3
# table["Steer"] = 4
# table["Setrika"] = 5
#
# # menampilkan hash table dari tas
# print(table["Tas"])
#
# #merubah nilai setrika menjadi 7
# table["Setrika"] = 7
# print( table)
#
# #Menghapus steer
# del table["Steer"]
# print(table)
