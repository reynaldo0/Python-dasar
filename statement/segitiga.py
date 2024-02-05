# Latihan perulangan membuat segitiga
sisi = 10

# 1. Menaggunakan For

# Dummy Variable
print("\n===== Awal Program For =====")

count = 1

for i in range(sisi):
    print("*"*count)
    count += 1

print("===== End Program For ===== \n")

# 2. Menggunakan While
print("===== Awal Program While =====")

count = 1

while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("===== End Program While ===== \n")

# 3. Hanya ganjil saja
print("===== Awal Program Ganjil =====")

count = 1

while True:
    if count%2:
        # Print jika Ganjil
        print("*"*count)
        count += 1
    else:
        # Akan kembali ke atas jika ganjil
        count += 1
        continue

    # Akan break jika count melebihi  sisi
    if count > sisi:
        break

print("===== End Program Ganjil ===== \n")


# 3. Hanya Genap saja
print("===== Awal Program Genap =====")

count = 1

while True:
    if count%2:
        # Akan kembali ke atas jika ganjil
        count += 1
        continue

    # Print jika Genap
    print("*"*count)
    count += 1

    # Akan break jika count melebihi  sisi
    if count > sisi:
        break

print("===== End Program Genap ===== \n")


# 4. Segitiga sama kaki
print("===== Awal Program Segitiga Sama Kaki =====")

count = 1
spasi = int(sisi/2)

while True:
    if count%2:
        # Akan kembali ke atas jika ganjil
        count += 1
        continue

    # Print jika Genap
    print(" "*spasi, "+"*count)
    count += 1
    spasi -= 1

    # Akan break jika count melebihi  sisi
    if count > sisi:
        break

print("===== End Program Segitiga Sama Kaki ===== \n")