# list_angka = [1,5,3,6,8,2,4,6,10]
# angka_baru = [item*2 for item in list_angka]
# print(angka_baru)

#generator
original_list = [1, 2, 3, 4, 5]
generator = (item * 2 for item in original_list)

print(next(generator))  # Output: 2
print(next(generator))  # Output: 4

# atau menggunakan perulangan for
generator = (item * 2 for item in original_list)
for value in generator:
    print(value)