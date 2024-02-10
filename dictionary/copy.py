# Copy dictionary

data_orang =  {
    "mah":"Bagas mahesa",
    "sub":"Bagus subang",
    "gus":"Agus Baruu",
    "cup":"Ucup Ajalah",
    "ra":"Inara Razana"
}

poeple = data_orang.copy()
print("="*25)
print(f"Data orang = \n{data_orang}")
print(f"Data Poeple = \n{poeple}\n")

print("="*25)
data_orang["mah"]="Mahesa Maulana"
print(f"Data orang = \n{data_orang}")
print(f"Data Poeple = \n{poeple}\n")

# Pop dictionary (Berdasarkan key)
print("="*25)
dataAgus = poeple.pop("gus")
print(f"Data agus = {dataAgus}")
print(f"Poeple = {poeple}\n")

# Pop item dictionary (yang terakhir, key dan value)
print("="*25)
lastData = poeple.popitem()
print(f"Data Terakhir = {lastData}")
print(f"Poeple = {poeple}\n")
