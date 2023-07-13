#recursion
def faktorial(n):
    if n == 1:
        return n
    else:
        return n*faktorial(n - 1)
nilai = int(input("Masukkan nilai : "))
faktorial(nilai)
print(faktorial(nilai))

#basic recursion
def countdown(n):
    if n == 0:  # Base case
        print("Selesai!")
    else:
        print(n)
        countdown(n - 1)  # Rekursif

countdown(nilai)