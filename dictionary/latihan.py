import datetime
import os
import string
import random

#Template Data Mahasiswa
mahasiswa_temp = {
    "nama":"nama",
    "nim":"000000",
    "sks_lulus":0,
    "lahir":datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    os.system("cls")
    print(f"{'SELAMAT DATANG':^30}")
    print(f"{'DATA MAHSISWA':^30}")
    print("-"*30)

    mahasiswa = dict.fromkeys(mahasiswa_temp.keys())
    mahasiswa['nama'] = input("Nama Lengkap \t\t: ")
    mahasiswa['nim'] = input("Nim \t\t\t: ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus \t\t: "))
    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY) \t: "))
    BULAN_LAHIR = int(input("Bulan Lahir (1 - 12) \t: "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (1 - 31) \t: "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"\n{"KEY":<7} {"NAMA":<20} {"NIM":<8} {"SKS":<3} {"LAHIR":<10}")
    print("-"*55)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%d %B %Y")

        print(f"{KEY:<7} {NAMA:<20} {NIM:<8} {SKS:<3} {LAHIR:<10}")

    print("\n")
    is_done = input("Lanjutkan Program (y/n)? = ")
    if is_done == "n":
        break

print("\nProgram selesai, Terimakasih")