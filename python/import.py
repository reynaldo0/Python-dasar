'''Import Statement'''

'''Menyambungkan Program dari external'''
import global_local

'''Import dengan namespace'''
import variable

# data ada di namespace variable 
print(variable.data)

'''Import dengan fungsi'''
import matematika

hasil = matematika.tambah(4,6)
print(hasil)