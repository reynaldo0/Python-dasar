# hasil = boolean / True/False

a = 4
b = 2

# Operasi >
print("\n #### Lebih Dari ####\n")
hasil  = a > 3
print(a, '>', 3, '=', hasil)

hasil  = b > 3
print(b, '>', 3, '=', hasil)

hasil  = b > 2
print(b, '>', 2, '=', hasil)

# Operasi <
print("\n #### Kurang Dari ####\n")
hasil  = a < 3
print(a, '<', 3, '=', hasil)

hasil  = b < 3
print(b, '<', 3, '=', hasil)

hasil  = b < 2
print(b, '<', 2, '=', hasil)

# Operasi >=
print("\n #### Lebih Dari Sama Dengan ####\n")
hasil  = a >= 3
print(a, '>=', 3, '=', hasil)

hasil  = b >= 3
print(b, '>=', 3, '=', hasil)

hasil  = b >= 2
print(b, '>=', 2, '=', hasil)

# Operasi <=
print("\n #### Kurang Dari Sama Dengan ####\n")
hasil  = a <= 3
print(a, '<=', 3, '=', hasil)

hasil  = b <= 3
print(b, '<=', 3, '=', hasil)

hasil  = b <= 2
print(b, '<=', 2, '=', hasil)

# Operasi ==
print("\n #### Sama Dengan ####\n")
hasil  = a == 4
print(a, '==', 4, '=', hasil)
hasil  = b == 4
print(b, '==', 4, '=', hasil)

# Operasi !=
print("\n #### Tidak Sama Dengan ####\n")
hasil  = a != 4
print(a, '!=', 4, '=', hasil)
hasil  = b != 4
print(b, '!=', 4, '=', hasil)

# Operasi IS (sebagai komperasi object identity)
print("\n #### Object Identity (IS) ####\n")
x = 5
y = 5
print('Nilai x = ', x, 'id = ', hex(id(x)))
print('Nilai y = ', y, 'id = ', hex(id(y)))
hasil = x is y
print("x is y = ", hasil)

x = 5
y = 8
print('Nilai x = ', x, 'id = ', hex(id(x)))
print('Nilai y = ', y, 'id = ', hex(id(y)))
hasil = x is y
print("x is y = ", hasil)

# Operasi IS NOT (sebagai komperasi object identity)
print("\n #### Object Identity (IS NOT) ####\n")
x = 5
y = 5
print('Nilai x = ', x, 'id = ', hex(id(x)))
print('Nilai y = ', y, 'id = ', hex(id(y)))
hasil = x is not y
print("x is y = ", hasil)

x = 5
y = 8
print('Nilai x = ', x, 'id = ', hex(id(x)))
print('Nilai y = ', y, 'id = ', hex(id(y)))
hasil = x is not y
print("x is y = ", hasil)