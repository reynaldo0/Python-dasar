# Kumpulan data number

data_angka = [1,2,3,4,5]
print(data_angka)

# Kumpulan data string
data_string = ["Agus, Warni, Warno"]
print(data_string)

# Kumpulan data Boolean
data_bool = [True, False, True]
print(data_bool)

# Kumpulan Campuran Data
data_campuran = [1, "Ketupat", 2, "Gorengan", 3, "Pop Ice",  False]
print((data_campuran))

# Cara alternatif membuat range
data_range = range(0,10,2)
data_list = list(data_range)
print(data_range)
print(data_list)

# Membuat list dengan for loop, list comprehersion
list_for = [i for i in range (0,15)]
print(list_for)
list_for_kuarat = [i**2 for i in range (0,15)]
print(list_for_kuarat)

# Membuat list pake For, IF
# Tidak sama dengan 5
list_if = [i for i in range(0,10) if i != 5]
print(list_if)

# LIST FOR IF GENAP
list_if_genap = [i for i in range(0,10) if i %2 == 0]
print(list_if_genap)

# LIST FOR IF GENAP KUADRAT
list_if_genap = [i**2 for i in range(0,10) if i %2 == 0]
print(list_if_genap)

# LIST FOR IF GANJIL
list_if_ganjil = [i for i in range(0,10) if i %2 != 0]
print(list_if_ganjil)

# LIST FOR IF GANJIL KUADRAT
list_if_ganjil = [i**2 for i in range(0,10) if i %2 != 0]
print(list_if_ganjil)