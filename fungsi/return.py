'''
def namafungsi(argument):
    Badan fungsi 
    return output
'''

def kuadrat(angka):
    #Fungsi Kuadrat
    output = angka**2
    return output

y = kuadrat(25)
print(y)

print(kuadrat(6))

z = 11 + kuadrat(10)
print(z)

# Fungsi tambah
def tambah(angka1, angka2):
    # Return dengan multi input
    return angka1 + angka2

x = tambah(15, 5)
print(x)

# Fungsi dengan return banyak
def operasi_mtk(angka1, angka2):
    plus = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return plus, kurang, kali, bagi

p,k,l,b = operasi_mtk(10, 2)
print(f"Hasil Tambah {p}")
print(f"Hasil Kurang {k}")
print(f"Hasil Kali {l}")
print(f"Hasil Bagi {b}")