# Memasukan data/argument

def fungsi(nama,tinggi,berat):
    print(f"{nama}, Tinggi = {tinggi}, dan Berat = {berat}")

fungsi("ucup",160,50)

def fungsi(data_list):
    data = data_list.copy()
    nama = data [0]
    tinggi = data [1]
    berat = data [2]
    print(f"{nama}, Tinggi = {tinggi}, dan Berat = {berat}")

fungsi(["udin", 190, 60])

# ARGS 
def args(*args):
    nama = args [0]
    tinggi = args [1]
    berat = args [2]
    print(f"{nama}, Tinggi = {tinggi}, dan Berat = {berat}")

args("lola",180,90)

# studi kasus data berkali kali

def tambah(*data):
    # Data tipenya adalah tuple, dan dia bisa di iterasi
    output = 0
    for angka in data:
        output += angka

    return output

hasil = tambah(1,2,3,4,5,6,7,8)
print(f"hasil = {hasil}")

hasil = tambah(100,25,45)
print(f"hasil = {hasil}")