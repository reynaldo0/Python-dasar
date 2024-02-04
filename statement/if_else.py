nama = input("Siapa nama Anda? ")
# if kondisi: aksi
# program selanjutnya

# Program IF inline
print("\n"+7*"=" + " Program IF inline " + "="*7)
print(f"Nama = " +nama)
if nama=="rara": print("Kamu Cantiik!!")
print(f"Terimakasih {nama}")

# Program if indentation
print("\n"+7*"=" + " Program if indentation " + "="*7)
print(f"Nama = " +nama)
if nama=="rara":
    print("Gokill!! Cantiknya!!")
    print("KECEE!!")
print(f"Terimakasih {nama}")

# Else statement
print("\n"+7*"=" + " Else Statement " + "="*7)
if nama=="ragil":
    print(f"Hai {nama} Kamu Keren")
else:
    print(f"Ohh {nama} Kamu biasa aja")
print(f"Terimakasih {nama}")

# Else If
print("\n"+10*"="+"Program ElIf "+10*"=")
if nama =="ucok": #Kondisi 1
    print(f"lah nama kamu {nama}") # Aksi true 1
elif nama =="ragil": # Kondisi 2
    print(f"Kamu {nama}, tapi tidak ucok") # Aksi True 2
elif nama =="aldo": # Kondisi 3
    print(f"oohh {nama}, Yang ganteng itu " + "wk"*5) # Aksi True 3
else: 
    print(f"Hah.. {nama} siapa lu?") # Aksi False
print(f"Terimakasih {nama} sudah mengisi")
