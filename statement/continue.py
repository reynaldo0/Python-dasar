# Continue, Pass

angka = 0

while angka < 5:
    angka += 1
    if angka ==3:
        print("Widiih")
        pass # Ini tidak akan di eksekusi
    print(angka)

# Continue
angka = 0

print(f"Angka sekarang ==> {angka}")
while angka < 5:
    angka += 1
    print(f"Angka sekarang ==> {angka}") # Aksi 1
    if angka == 3:
        print("Keren!!")
        continue # Akan membuat loop loncat ke step selanjutnya
    print("WhatsUpp") # Aksi 2
print("Finish Looping!!")