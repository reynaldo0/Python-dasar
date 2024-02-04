# Widh dan Multiline
# Data
data_nama = "Rizal"
data_umur = 17
data_tinggi = 169.5
data_no_sepatu = 44

# String standar
data_string = f"nama = {data_nama}, Umur = {data_umur}, Tinggi = {data_tinggi}, Nomor Sepatu = {data_no_sepatu}"
print(5*"=" + " DATA "+"="*5)
print(data_string)

# String multiline
data_string = f"nama = {data_nama},\nUmur = {data_umur},\nTinggi = {data_tinggi}, \nNomor Sepatu = {data_no_sepatu}"
print("\n" + 5* "=" + " DATA "+"="*5)
print(data_string)

# String multiline (Kutip Triplets)
data = f"""
data_nama = "Rizal"
data_umur = 17
data_tinggi = 169.5
data_no_sepatu = 44
"""

print("\n" + 5* "=" + " DATA KUTIP 3 "+"="*5)
print(data)

# Mengatur lebar
data_string = f"""
Nama    = {data_nama:>6}
Umur    = {data_umur:>6}
Tinggi  = {data_tinggi:>6}
Sepatu  = {data_no_sepatu:>6}
"""

print("\n" + 5* "=" + " DATA KUTIP 3 "+"="*5)
print(data_string)