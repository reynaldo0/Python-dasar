# konversi celcius ke satuan lain
print("\n #### PROGRAM KONVERSI TEMPERATUR ####\n")

celcius = float(input('Masukan suhu dalam celcius : '))
print('suhu adalah = ', celcius, "Celcius")

# Reamur
reamur = (4/5) * celcius
print('Suhu dalam Reamur adalah', reamur, "Reamur")

# Fahrenheit
fahrenheit = (9/5) * celcius + 32
print('Suhu dalam Fahrenheit adalah', fahrenheit, "Fahrenheit")


# Kelvin
kelvin = celcius + 273
print('Suhu dalam Kelvin adalah', kelvin, "Kelvin")