# Looping dari list

# For Loop
print("===== FOR LOOP DAN RANGE======")
list_angka = [1,5,4,2,6]

for angka in list_angka:
    print(f"Angka = {angka}")

peserta = ["Wahyu", "Asep", "Didit", "Deddy"]

for name in peserta:
    print(f"Nama = {name}")

# For loop dan Range
print("\n===== FOR LOOP DAN RANGE======")
list_angka = [1,7,8,2,9,10]
panjang = len(list_angka)

for i in range(panjang):
    print(f"Angka = {list_angka[i]}")

# While 
print("\n===== WHILE LOOP ======")
list_angka = [1,7,8,2,9,10]
panjang = len(list_angka)

i = 0

while i < panjang:
    print(f"Angka = {list_angka[i]}")
    i += 1

# List Comprehension
print("\n===== LIST COMPREHENSION ======")
data = ["ucup", 1, 2, 3, "udin"]

[print(f"Data =  {i}")for i in data]
angka = [1,7,8,2,9,10]

angka_kuadrat = [i**2 for i in angka]
print(f"Angka Kuadrat = {angka_kuadrat}")

# Enumerate
print("\n===== ENUMERATE ======")
data_list = ["ucup", 1, 2, 3, "udin"]

for index,data in enumerate(data_list):
    print(f"index = {index} - Data = {data}")