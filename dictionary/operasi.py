# Operator Dictionary

data_dict = {
    "ram":"Ramadina",
    "ki":"Niki chan",
    "pan":"Irfan surip",
}

# Panjang dictionary
lendict = len(data_dict)
print(f"Panjang dari dictionary = {lendict}")

# Mengecek key exist atau tidak
KEY = "ram"
CHECKKEY = KEY in data_dict
print(f"apakah '{KEY}' ada dalam dictionary? : {CHECKKEY}")

# Mengakses value / read menggunakan get
print(data_dict["ki"])
print(data_dict.get("pan"))
print(data_dict.get("rara","Tidak ada")) # Mengecek key ada / tidaknya

# Mengupdate data
data_dict["pan"] = "Irfan Sukabirus Mak"
print(f"Data di update = \n{data_dict}")

# Menambahkan data
data_dict["yat"] = "Dayat hidayat"
print(f"Data diubah menjadi = \n{data_dict}")

# Mengupdate data leebih simple
data_dict.update({"pan":"Irfan surip"}) # Jika Key sudah ada maka di ganti
print(f"Data di update = \n{data_dict}")

data_dict.update({"rey":"Reynaldo Yusellino"}) # Kalau gak ada di ambah dengan ototmatis
print(f"Data di update = \n{data_dict}")

# Menghapus data
del data_dict["rey"] 
print(f"Data di Dihapus = \n{data_dict}")