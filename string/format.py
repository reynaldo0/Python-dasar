nama = "agung"
format_str = f"hello {nama}"

print(format_str)

# Boolean
boolean = True
format_str = f"Boolean = {boolean}"
print(format_str)

# Angka
angka = 2005.5
format_str = f"Angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"Bilangan bulat = {angka:d}"
print(format_str)

# Bilangan ribuan
angka = 5000000
format_str = f"Angka Jutaan = {angka:,}"
print(format_str)

# Bilangan desima;
angka = 2005.54321
format_str = f"Desimal = {angka:.2f}"
print(format_str)

# Menampilkan leading zero
angka = 2005.54321
format_str = f"Desimal = {angka:011.2f}"
print(format_str)

# Menampilakn tanda + dan -
minus = -10
plus = 10
format_minus = f"minus = {minus:+d}"
format_plus = f"plus = {plus:+d}"

print(format_minus)
print(format_plus)

# Memformat persen
persen = 0.045
format_persen = f"Persen =  {persen:.2%}"
print(format_persen)

# Melakukan operasi aritmatika di dalam kurawal
harga = 10000
jumlah = 5
format_str = f"harga total = Rp. {harga*jumlah:,}"
print(format_str)

# Format angka lain (binary, octal, hexadesimal)
angka = 225
format_binary = f"Binary = {bin(angka)}"
format_octal = f"Octal = {oct(angka)}"
format_hex = f"Hexadesimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)