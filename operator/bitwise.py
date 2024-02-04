
a = 9
b = 5

# Bitwise OR (|)
c = a | b
print ("\n==== OR ====")
print ('Nilai = ', a, 'Binary = ', format(a,'08b'))
print ('Nilai = ', b, 'Binary = ', format(b,'08b'))

print ("\n==== (|) ====")
print ('Nilai = ', c, 'Binary = ', format(c,'08b'))

# Bitwise AND (&)
c = a & b
print ("\n==== AND ====")
print ('Nilai = ', a, 'Binary = ', format(a,'08b'))
print ('Nilai = ', b, 'Binary = ', format(b,'08b'))

print ("\n==== (&) ====")
print ('Nilai = ', c, 'Binary = ', format(c,'08b'))

# Bitwise XOR (^)
c = a ^ b
print ("\n==== XOR ====")
print ('Nilai = ', a, 'Binary = ', format(a,'08b'))
print ('Nilai = ', b, 'Binary = ', format(b,'08b'))

print ("\n==== (^) ====")
print ('Nilai = ', c, 'Binary = ', format(c,'08b'))

# Bitwise NOT (~)
c = ~a 
print ("\n==== NOT ====")
print ('Nilai = ', a, 'Binary = ', format(a,'08b'))

print ("\n==== (~) ====")
print ('Nilai = ', c, 'Binary = ', format(c,'08b'))

print ("\n==== (^) ====")
d = 0b00001001
e = 0b11111111

print('Nilai = ', e^d, 'Binary = ', format(e^d,'08b'))

# Shifting (Shift Right)
c = a >> 1
print ("\n==== Shift Right ====")
print ('Nilai = ', a, 'Binary = ', format(a,'08b'))

print ("\n==== (>>) ====")
print ('Nilai = ', c, 'Binary = ', format(c,'08b'))

# Shifting (Shift Left)
c = a << 2
print ("\n==== Shift Left ====")
print ('Nilai = ', a, 'Binary = ', format(a,'08b'))

print ("\n==== (<<) ====")
print ('Nilai = ', c, 'Binary = ', format(c,'08b'))
