# Default argumen

"""
def fungsi(argument):
def fungsi(argument = nilai default):
""" 

# 1. Penulisan dan penggunaan default argument
def say_hi(nama = "manis"):
    # Fungsi dengan default argument
    print(f"Hallo {nama}")

say_hi("ucup")
say_hi()

# 2. Jika tidak didefinisikan, maka akan menggunakan nilai default yang telah ditentukan.
def say_he(nama,pesan = "Apa kabar"):
    # Fungsi dengan satu input biasa dan satu default argument
    print(f"hai {nama}, {pesan}")
say_he("Agus", "Hai cowok")
say_he("agus")

# 3. Tidak boleh menyertakan default argument dengan parameter lainnya yang memiliki jenis data yang sama.
def hitung_pangkat(angka,pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,5))

hasil = hitung_pangkat(angka=5, pangkat=2)
print(hasil)

# 4. Argument yang ingin di rubah
def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=10))