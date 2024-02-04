a = 10
b = 3

# Operasi Tambah
hasil = a + b 
print(a, "+", b, "=", hasil)

# Operasi Kurang
hasil = a - b 
print(a, "-", b, "=", hasil)

# Operasi Kali
hasil = a * b 
print(a, "*", b, "=", hasil)

# Operasi Bagi
hasil = a / b 
print(a, "/", b, "=", hasil)

# Operasi Eksponen / Pangkat
hasil = a ** b 
print(a, "**", b, "=", hasil)

# Operasi Modulus / Sisa  Bagi
hasil = a % b 
print(a, "%", b, "=", hasil)

# Operasi Floor Division
hasil = a // b 
print(a, "//", b, "=", hasil)

# Prioritas operasi, operational predence
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print (x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, hasil)

hasil = x + y * z
print('Tambah semua : ',x, '+', y ,'+' ,z ,'=', hasil)

# () Dewa
hasil = (x + y) * z
print('Tambah semua : ' '(',x, '+', y, ')','*' ,z ,'=', hasil)