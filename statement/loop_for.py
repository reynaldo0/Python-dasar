# Perulangan (Looping)

# for kondisi:
#     aksi

# Contoh dengan List
angka_list = [0,2,4,6,8,10]
print(angka_list)

for i in angka_list:
    print(f"i sekarang ==>{i}")
print(f"Ini akhir dari program 1\n")

# Contoh dengan range
angka_range = range(5)

for i in angka_range:
    print(f"i sekarang ==>{i}")
print(f"Ini akhir dari program 2\n")

# Contoh dengan range dengan pembatas
angka_range = range(1,10)

for i in angka_range:
    print(f"i sekarang ==>{i}")
    print("Saya keren")
print(f"Ini akhir dari program 3\n")

# Menggunakan string
data_str = "Kamu keren abis"

for huruf in data_str:
    print(huruf)
print(f"Ini akhir dari program 4\n")