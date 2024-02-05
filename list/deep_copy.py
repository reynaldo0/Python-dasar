data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0, data_1, 10]
data_2D_copy = data_2D.copy()

print(f"Data = {data_2D}")
print(f"Data copy = {data_2D_copy}")

# Mengambil data
data = data_2D[0]
print(f"Data Pertama = {data}")

data = data_2D[0][0]
print(f"Data Paling Pertama = {data}")

# Addres smuanya
print(f"Data 2D Asli = {hex(id(data_2D))}")
print(f"Data 2D Copy = {hex(id(data_2D_copy))}")

print("Addres dari member ke 1")
print(f"Data 2D Asli = {hex(id(data_2D[0]))}")
print(f"Data 2D Copy = {hex(id(data_2D_copy[0]))}")

data_2D[1][0] = 5
data_2D[2] = 8
print(f"Data = {data_2D}")
print(f"Data copy = {data_2D_copy}")

# Deep Copy
from copy import deepcopy

data_2D = [data_0, data_1, 10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"Data 2D Asli = {hex(id(data_2D))}")
print(f"Data 2D Copy = {hex(id(data_2D_deepcopy))}")

print("address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_deepcopy[0]))}")

data_2D[1][0] = 30
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deep = {data_2D_deepcopy}")