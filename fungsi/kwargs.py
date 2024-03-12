'''**kwargs'''

def fungsi(nama,tinggi,berat):
    '''Fungsi Biasa'''
    print(f"Nama = {nama}, Tinggi = {tinggi}, Berat = {berat}")

fungsi("Udin", 190, 90)

def fungsi(**kwargs):
    '''Fungsi Directionary'''
    print(kwargs["nama"])

fungsi(nama = "Ujang", tinggi = 100, berat = 1)

def fungsi(**kwargs):
    '''Fungsi Kwargs'''
    nama = kwargs ["nama"]
    tinggi = kwargs ["tinggi"]
    berat = kwargs ["berat"]
    print(f"Nama = {nama}\nTinggi = {tinggi}\nBerat = {berat}")

fungsi(nama = "Ujang", tinggi = 100, berat = 1)

# Studi kasus
def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("Tidak ada operasi")
    return output

tambah = math(1,2,3,4,5,6,7, option="tambah")
print(f"Hasil jumlah {tambah}")
kali = math(1,2,3,4,5,6,7, option="kali")
print(f"Hasil kali {kali}")