print(10*"=" + " Kalkulator Sederhana " + "="*10+ "\n")

angka_1 = float(input("Masukan Angka 1 = "))
angka_2 = float(input("Masukan Angka 2 = "))
operator = input("Operator (+,-,x,/) = ")

# Percabangan
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah {hasil}")

elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah = {hasil}")

elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah = {hasil}")

elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah = {hasil}")
else:
    print("Operator yang anda masukan tidak Valid!")