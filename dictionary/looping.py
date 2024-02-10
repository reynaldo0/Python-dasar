# Looping dictionary

data_manusia = {
    "al":"Al Farizi",
    "tong":"Otong Markotong",
    "jal":"Rijal Markojal",
    "Rey":"Rerey Markoray",
    "Zid":"Zidane Tiran"
}

# Looping "Yang keluar Key nya"
print("\n ==================")
for manusia in data_manusia:
    print(f"Nama Manusia (Key) = {manusia}")

# Operator mengambil item / Iterable
print("\n ==================")
keys = data_manusia.keys()
print(f"Nama Manusia (Key) = {keys}")

print("\n ==================")
for key in data_manusia.keys():
    print(f"Nama manusia Value = {data_manusia.get(key)}")

print("\n ==================")
values = data_manusia.values()
print(f"Semua Nama Manusia (Value) = {values}")

print("\n ==================")
for value in data_manusia.values():
    print(f"Data Value = {value}")

#Items Loop
print("\n ==================")
items = data_manusia.items() # Berantakan
print(f"Items = \n{items}")

print("\n ==================")
for items in data_manusia.items(): # Lebih rapih
    print(f"Items = {items}")

print("\n ==================")
for key,value in data_manusia.items():
    print(f"Key = {key} - Values {value}")