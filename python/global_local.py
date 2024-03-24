'''Global dan local scope'''

nama_global = "ucup" # <- Variable Global

'''Akses variable global dalam fungsi'''
def fungsi1():
    print(f"Nama = {nama_global}")

fungsi1()

'''Akses variable global dalam loop'''
for i in range(0,8):
    print(f"loop {i}: Nama = {nama_global}")

'''Akses variable global dalam Percabangan'''
if True:
    print(f"Menampilkan = {nama_global}")


'''Variable Local Scope'''
def fungsi2():
    nama_local = "Jordy" # <- Variable Local 
    print(f"Nama Local = {nama_local}")
fungsi2()

'''Contoh 1 Penggunaan'''
def say_ular():
    print(f"Hello {nama}")

nama = "ular"
say_ular()

'''Contoh 2 Penggunaan'''
angka = 0
nama = "Agus"

def ubah(niba, naba):
    global angka # Mendapatkan akses untuk merubah angka
    global nama

    angka = niba
    nama = naba

print(f"Sebelum = {angka, nama}")
ubah(10, "Dufan")
print(f"Sesudah = {angka, nama}")

'''Contoh 3 Penggunaan'''

angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 100
    angka_dummy = 10

print(angka)
print(angka_dummy)