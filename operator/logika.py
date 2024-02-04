# Not, Or, And, Xor

# Operator NOT adalah kebalikan dari nilainya
print('\n ==== NOT ====\n')
a = True
c = not a
print('Data A Bernilai = ', a)
print('== NOT ==')
print('Data C Bernilai = ', c)

# Operator OR (True jika salah satu dari dua operand berisi nilai True)
print('\n ==== OR ====\n')
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)

a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)

a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)

a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)

# Operator AND (True jika semua operand berisi nilai True)
print('\n ==== AND ====\n')
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)

a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)

a = False
b = True
c = a and b
print(a, 'AND', b, '=', c)

a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)

# Operator XOR  (True jika salah satu operand berisi nilai True)
print('\n ==== XOR ====\n')
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)

a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)

a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)

a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)