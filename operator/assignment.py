# Operasi yang dapat dilakukan dengan penyingkatan

print('\n=== ARITMATIKA ===')
a = 5 # Disebut Assignment
print('Nilai A = ', a)

a += 3 # artinya adalah a = a + 1
print('Nilai A += 3, Nilai  A = ', a)

a -= 4 # artinya adalah a = a - 4
print('Nilai A -= 4, Nilai  A = ', a)

a *= 5 # artinya adalah a = a * 5
print('Nilai A *= 5, Nilai  A = ', a)

a /= 10 # artinya adalah a = a / 10
print('Nilai A /= 10, Nilai  A = ', a)

b = 10
print('\nNilai B = ', b)

# Modulus dan Floor Division
b %= 3
print('Nilai B %= 3, Nilai  B = ', b)

b = 10
print('\nNilai B = ', b)

b //= 3
print('Nilai B //= 3, Nilai  B = ', b)

a = 5
print('\nNilai A = ', a)

# Pangkat atau eksponen
a **= 3
print('Nilai A **= 3, Nilai  A = ', a)

print('\n\n=== OPERASI BITWISE ===')
print('\nOR')
c = True
print('Nilai c = ', c)
c |= False
print('Nilai C |= False, Nilai  C = ', c)

c = False
print('Nilai c = ', c)
c |= False
print('Nilai C |= False, Nilai  C = ', c)

print('\nAND')
c = True
print('Nilai c = ', c)
c &= False
print('Nilai C &= False, Nilai  C = ', c)

c = True
print('Nilai c = ', c)
c &= True
print('Nilai C &= True, Nilai  C = ', c)

print('\nXOR')
c = True
print('Nilai c = ', c)
c ^= False
print('Nilai C ^= False, Nilai  C = ', c)

c = True
print('Nilai c = ', c)
c ^= True
print('Nilai C ^= True, Nilai  C = ', c)

# Binary
print('\nBINARY')
d = 0b0100
print('Nilai D = ', format(d,'04b'))

d >>= 2
print('Nilai D >>= 2, Nilai  D = ', format(d,'04b'))

d <<= 1
print('Nilai D <<= 1, Nilai  D = ', format(d,'04b'))
