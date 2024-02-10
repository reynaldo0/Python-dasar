# Fungsi dengan argument (Input)

'''
def namafungsi(argument):
    Badan fungsi 
'''
def hello_world(nama):
    # Fungsi hello world menerima input dengan variable nama
    print(f"Selamat datang {nama}")

hello_world("Udin")
hello_world("Yanto")

# program tambah

def tambah(angak_1, angka_2):
    hasil = angak_1 + angka_2
    print(f"{angak_1} + {angka_2} = {hasil}")

tambah(1,8)
tambah(1000,100)

def manusia(human): 
    data_human = human.copy()
    for orang in human:
        print(f"Yang terhormat {orang}")
        
anggota = ["Ucok", "Rafli", "Fihzal"]

manusia(anggota)