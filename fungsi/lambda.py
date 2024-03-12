'''Lamda Function'''

'''Fungsi Biasa'''
def f_kuadrat(angka):
    return angka**2

print(f"Hasil fungsi kuadrat = {f_kuadrat(4)}")

'''Fungsi Lamda'''
'''Output = lamda argumen:expression'''
kuadrat = lambda angka:angka**2
print(f"Hasil lambda kuadrat = {kuadrat(3)}")

pangkat = lambda num,pow : num**pow
print(f"Hasil lamda pangkat = {pangkat(4,2)}")

# Sorting untuk list berdasarkan alfabet
data_list = ["Kakaa","Kikiii","Kuku"]
data_list.sort()
print(f"Sort Alfabet = {data_list}")

# Sorting untuk list berdasarkan panjang
data_list.sort(key=len)
print(f"Sort Panjang = {data_list}")

# menggunakan fungsi
def len_nama(nama):
    return len(nama)

data_list.sort(key=len_nama)
print(f"Sort Panjang dengan fungsi = {data_list}")

'''Sorting menggunakan Lambda'''
data_list = ["Kakaa","Kikiii","Kuku"]
data_list.sort(key=lambda nama:len(nama))
print(f"Sort Panjang dengan lambda = {data_list}")

'''Filter'''
data_angka = [1,2,3,6,7,9,11,12,13,15]
def kurang_lim(angka):
    return angka < 5
data_angka_new = list(filter(kurang_lim,data_angka))
data_angka_new = list(filter(lambda x : x>5, data_angka))
print(data_angka_new)

# Kasus Genap 
data_genap = list(filter(lambda x : (x%2==0),data_angka))
print(data_genap)

# Kasus Ganjil 
data_ganjil = list(filter(lambda x : (x%2!=0),data_angka))
print(data_ganjil)

# Kelipatan 3
data_tiga = list(filter(lambda x : (x%3==0),data_angka))
print(data_tiga)

