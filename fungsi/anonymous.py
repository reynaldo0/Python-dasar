'''Anonymous Function'''

'''Fungsi Biasa'''
def pangkat(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,2)
print(f"Fungsi Biasa = {data_hasil}")

'''Currying'''
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"Pangkat 2 dari 5 = {pangkat2(5)}")

pangkat3 = pangkat(3)
print(f"Pangkat 3 dari 10 = {pangkat3(10)}")

print(f"Pangkat Bebas = {pangkat(4)(5)}")