# Membuat gabungan area rentang dari angka

user = float(input("Masukan angka yang bernilai \nkurang dari 3 atau lebih dari 10 = "))

# Membuat input Kurang Dari 3
isKurangDari = (user < 3)
print ("Kurang Dari 3 = ", isKurangDari)

# Membuat input lebih Dari 10
print('\n IRISAN \n')
isLebihDari = (user > 10)
print("Lebih Dari 10 = ", isLebihDari)

isCorrect = isKurangDari or isLebihDari
print('Angka yang anda masukan = ', isCorrect)

user = float(input("Masukan angka yang bernilai \nlebih dari 3 dan kurang dari 10 = "))
# Lebih dari 3
isLebihDari = (user > 3)
print('Lebih dari 3 = ', isLebihDari)

isKurangDari = (user < 10)
print('Kurang dari 10 = ', isKurangDari)

isCorrect = isKurangDari and isLebihDari
print('Angka yang anda masukan = ', isCorrect)
