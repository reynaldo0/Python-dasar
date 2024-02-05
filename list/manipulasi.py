# Operasi

# Index  0(-3)   1(-2)    2(-1)
data = ["Gajah", "Jerapah", "Kambing"]

# Mengambil data dari list
data_0 = data[0]
print(f"Data pertama (Index 0) = {data_0}")

data_terakhir = data[-1]
print(f"Data Terakhir Adalah = {data_terakhir}")

data_Gajah = data[-3]
print(f"Data Gajah adalaha = {data_Gajah}")

# Mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"Panjang data adalah = {panjang_data}")

# Manipulasi data list

# MENAMBAHKAN ITEM PADA LIST
print(f"Data sebelum di tambah = \n{data}")
data.insert(1, "Zebra")
print(f"Data sesudah di tambahkan = \n{data}")

# MENAMBAHKAN ITEM DI AKHIR LIST
data.append("Kucing")
print(f"Data sesudah di tambahkan = \n{data}")

# Menambahkan List dengan list
data_baru =["Kelinci", "Dinasaurus", "Burung"]
data.extend(data_baru)
print(f"Data Gabungan = \n{data}")

# Merubah data
# Data Kelinci di ubah menjadi beruang
data[-3] = "Beruang"
print(f"Data dirubah menjadi = \n{data}")

# Menghilangkan data
data.remove("Kucing")
print(f"Data remove menjadi = \n{data}")

# Menghapus data paling akhir
data_akhir = data.pop()
print(f"Data akhir remove menjadi = \n{data}")
print(data_akhir)