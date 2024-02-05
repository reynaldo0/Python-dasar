data_angka = [1,2,4,1,4,5,1,7,1,8,1,9,2]

print(f"Data angka = \n{data_angka}")

# count angka
jumlah_1 = data_angka.count(1)
print(f"Jumlah angka 1 = {jumlah_1}")

# Ambil posisi data (Index)
data = ["kambing", "sapi", "zebra", "ular"]
print(f"Data = {data}")

index_sapi =data.index("sapi")
index_zebra =data.index("zebra")
print(f"Posisi si Sapi = {index_sapi}")
print(f"Posisi si zebra = {index_zebra}\n")

# Mengurutkan List angka terkecil ke terbesar
print(f"Data angka sebelum sort = {data_angka}")
data_angka.sort()
print(f"Data angka sort = {data_angka}\n")

# String diurutkan berdasarkan A-Z
print(f"Data sebelum sort = {data}")
data.sort()
print(f"Data angka sort = {data}")

# Balik listnya Z-A
data_angka.reverse()
data.reverse()
print(f"\nData angka setelah reverse = {data_angka}")
print(f"Data setelah reverse = {data}")