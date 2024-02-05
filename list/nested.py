# List bersarang

data_0 = [1,2]
data_1 = [3,4]

data_biasa = [1,2,3,4]

print(f"List biasa = {data_biasa}")

list_2D = [data_0, data_1,5,6]
print(f"List 2D = {list_2D}")

# Contoh penggunaan
peserta_0 = ["Ucup",25,"Laki-laki"]
peserta_1 = ["Wibu",200,"Laki-laki"]
peserta_2 = ["Rara",16,"Wanita"]

list_peserta =[peserta_0, peserta_1, peserta_2]
print (f"Peserta = {list_peserta}\n")

for peserta in list_peserta:
    print(f"Nama\t\t = {peserta[0]}")
    print(f"Umur\t\t = {peserta[1]}")
    print(f"Jenis Kelamin\t = {peserta[2]}\n")
print("Akhir dari program")

# Dengan reference
list_copy = list_peserta.copy()
print (f"Peserta = {list_copy}\n")
peserta_0[0] = "Agus"
print (f"Peserta = {list_copy}\n")
print (f"Peserta = {list_peserta}\n")
    
