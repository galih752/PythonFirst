import heapq
# membuat variabel penampung
heap = []
# memasukkan nilai
heapq.heappush(heap,1)
heapq.heappush(heap, 7)
heapq.heappush(heap,5)
heapq.heappush(heap,2)
print(heap)
# menghapus nilai yang paling kecil
smallest = heapq.heappop(heap)
# menampilkan nilai yang sudah dihapus
print (heap)
# merubah data menjadi dimulai dari angka yang kecil
ubah = [5,3,2,7,4]
heapq.heapify(ubah)
print(ubah)
# mencari 4 nilai terkecil
small = heapq.nsmallest(4,ubah)
print(small)
#Mencari 4 nilai terbesar
larg = heapq.nlargest(4,ubah)
print(larg)


#stack
stuck = []
stuck.append(50)
stuck.append(60)
stuck.append(40)
stuck.append(20)
stuck.append(30)

#menghapus nilai yang terakhir dimasukkan
top = stuck.pop()
print(stuck)
