import os

# Program menghitung luas & kelilig persegi panjang
# os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# Mengambil input user
# LEBAR = int(input("Masukan nilai Lebar = "))
# PANJANG = int(input("Masukan nilai Panjang = "))

# Program menghitung luas
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# Tampilkan hasilnya
# print(f"Hasil perhitungan Luas = {LUAS}")
# print(f"Hasil perhitungan Keliling = {KELILING}")

def header():
    # HEADER
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''FUNGSI INPUT USER'''
    # Mengambil input user
    lebar = int(input("Masukan nilai Lebar = "))
    panjang = int(input("Masukan nilai Panjang = "))
    return lebar, panjang

def hitung_luas(lebar,panjang):
    '''Fungsi Luas'''
    return lebar*panjang

def hitung_keliling(lebar, panjang):
    '''Fungsi Keliling'''
    return 2*(lebar + panjang)

def display(massage, value):
    '''Fungsi display'''
    print(f"Hasil perhitungan {massage} = {value}")

while True:
    header()

    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)

    display(f"Luas = ", LUAS)
    display(f"Keliling = " ,KELILING)

    isContinue = input("Hentikan Program (y/n)? = ")
    if isContinue == "y":
        break
print("Program selesai")
