# merubah satu tipe data ke tipe data lain

# INTEGER
print("CASTING DATA INTEGER")
data_int = 12
print ("Nilai tipe data : ", data_int, "bertipe data : ", type(data_int))

# CASTING 
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #false = 0
print ("Nilai tipe data : ", data_float, "bertipe data : ", type(data_float))
print ("Nilai tipe data : ", data_str, "bertipe data : ", type(data_str))
print ("Nilai tipe data : ", data_bool, "bertipe data : ", type(data_bool))

# FLOAT
print("CASTING DATA FLOAT")
data_float = 12.5
print ("Nilai tipe data : ", data_float, "bertipe data : ", type(data_float))

# CASTING
data_int = int(data_float) #akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float) #false = 0
print ("Nilai tipe data : ", data_int, "bertipe data : ", type(data_int))
print ("Nilai tipe data : ", data_str, "bertipe data : ", type(data_str))
print ("Nilai tipe data : ", data_bool, "bertipe data : ", type(data_bool))

# BOOLEAN
print("CASTING DATA BOOLEAN")
data_bool = True
print ("Nilai tipe data : ", data_bool, "bertipe data : ", type(data_bool))

# CASTING
data_int = int(data_bool) #akan dibulatkan kebawah
data_str = str(data_bool)
data_float = float(data_bool) 
print ("Nilai tipe data : ", data_int, "bertipe data : ", type(data_int))
print ("Nilai tipe data : ", data_str, "bertipe data : ", type(data_str))
print ("Nilai tipe data : ", data_float, "bertipe data : ", type(data_float))

# STRING
print("CASTING DATA STRING")
data_str = "100"
print ("Nilai tipe data : ", data_str, "bertipe data : ", type(data_str))

# CASTING
data_int = int(data_str) #String harus angka
data_float = float(data_str) 
data_bool = bool(data_str) #false = String Kosong
print ("Nilai tipe data : ", data_int, "bertipe data : ", type(data_int))
print ("Nilai tipe data : ", data_float, "bertipe data : ", type(data_float))
print ("Nilai tipe data : ", data_bool, "bertipe data : ", type(data_bool))