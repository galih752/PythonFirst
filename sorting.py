#Sorting Bubble_sort
def bubble_sort(arr):
    nilai = len(arr)
    for i in range(nilai):
        for j in range(nilai - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

data = [5, 2, 8, 1, 6,100,-1]
hasil = bubble_sort(data)
print(hasil)