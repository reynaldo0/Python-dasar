#Teknik menduplikat list

a = ["Zebra", "Kucing", "Harimau"]
print(f"A = {a}")

b = a # Pass by reference
print(f"B = {b}")

# Merubah member dari A

# MERUBAH KEDUA LIST
a[1] = "Kodok"
b.sort()
print(f"A = {a}")
print(f"B = {b}")

# Address dari kedua list a dan b
print(f"Address A = {hex(id(a))}")
print(f"Address B = {hex(id(b))}")

# Menduplikat List dengan Copy
print("Membuat list c dengan a.copy()")
c = a.copy() # Full duplikat / data baru

print(f"Address A = {hex(id(a))}")
print(f"Address B = {hex(id(b))}")
print(f"Address C = {hex(id(c))}")

print(f"A = {a}")
print(f"B = {b}")
print(f"C = {c}")

print("\nUbah data 0")
c[0] = "Katak"

print(f"A = {a}")
print(f"B = {b}")
print(f"C = {c}")

print("\nUbah data 1")
c[1] = "Kucing"

print(f"A = {a}")
print(f"B = {b}")
print(f"C = {c}")