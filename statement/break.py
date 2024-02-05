# STATEMENT BREAK

# CONTOH 1
print("\n" + 10*"=" + " Contoh Pertama " + 10*"=")

angka = 0

while angka < 5:
    angka += 1
    print(f"Angka Ke ==> {angka}")

    if angka == 4:
        print("Stooop")
        break
    print("Hallo Guys")
print("Akhir Program 1")

# CONTOH 2
print("\n" + 10*"=" + " Contoh Kedua " + 10*"=")
data_int = int(input("Hitung sampai = "))

angka = 0

while True:
    angka += 1
    print(f"Count = {angka}")

    if angka == data_int:
        print("Stooop")
        break
    print("Hallo Guys")
print("Akhir dari program 2")