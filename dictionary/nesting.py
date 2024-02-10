# Multi keys & Dictionary
import datetime

mahasiswa1 = {
    "nama":"Ahmad Saugi", 
    "nim":"1000129",
    "sks_lulus":120,
    "beasiswa":False,
    "lahir":datetime.datetime(2015,7,6)
}

mahasiswa2 = {
    "nama":"Laura Dwi", 
    "nim":"1000130",
    "sks_lulus":130,
    "beasiswa":True,
    "lahir":datetime.datetime(2010,10,10)
}

mahasiswa3 = {
    "nama":"Inara Lah", 
    "nim":"1000131",
    "sks_lulus":140,
    "beasiswa":True,
    "lahir":datetime.datetime(2007,4,13)
}

data_mahasiswa = {
    "MAH1":mahasiswa1,
    "MAH2":mahasiswa2,
    "MAH3":mahasiswa3,
} 

print(f"{"KEY":<4} {"NAMA":<20} {"SKS":<3} {"BEASISWA":<9} {"LAHIR":<10}")
print("-"*55)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%d %B %Y")
    print(f"{KEY:<4} {NAMA:<20} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")