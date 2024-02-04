# Menyambungkan string (Concatenate)
nama_pertama = "Rizal "
nama_kedua = "D'"
nama_ketiga = "Raur"

nama_lengkap = nama_pertama + nama_kedua + nama_ketiga
print(nama_lengkap)

# Menghitung panjang String
panjang = len(nama_lengkap)
print("Karakter yang terdapat dalam string ada", panjang, "karakter.")

# Mengecek apakah ada karakter di string dalam string
d = "D'R"
status = d in nama_lengkap
print("Apakah ada huruf",d, "di nama lengkap :", status)

d = "R'D"
status = d not in nama_lengkap
print("huruf",d, "tidak ada di nama lengkap :", status)

# Mengulang string
print("wk"*10)
print(15*"wk")

# Indexing
print("Index ke 0," + nama_lengkap[0])
print("Index ke 12," + nama_lengkap[10])
print("Index ke (-1)" + nama_lengkap[-1])
print("Index ke [0,2,4,6,8,10] " + nama_lengkap[0:10:2])

# item paling kecil
print("Item paling kecil : ", min(nama_lengkap))
# item paling besar
print("Item paling besar : ", max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah = " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah = " + chr(data))

# Operator dalam bentuk method
data = "rizalmulk rizaludin"
jumlah = data.count("l")
print("Jumlah 'l' didalam string =", jumlah)

# Merubah dari case ke string
# to uppercase
salam = "hallo bro whatsapp, welcome!"
print("normal = ", salam)
salam = salam.upper()
print("upper = ", salam)

# to lowecase
alay = "HalLO BrO WhaTsaPp, WeLCoMe!"
print("normal = ", alay)
salam = alay.lower()
print("lower = ", salam)

# Pengecekan dengan isX method
# pengecekan lower
salam = "hallo cuy whatsapp, welcome!"
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <- kegunaannya untuk mengecek semuanya huruf
# isalnum() <- kegunannnya untuk huruf dan angka
# isdesimal() <- angka saja
# isspace() <- spasi, tab, newline
# istitle() <- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title? = " + str(cek_judul))

# Ngecek komponen startswith() endswith()
cek_start = "Sangkuriang Padang".startswith("Sangkuriang")
print("starts = ", cek_start)

cek_ends = "Sangkuriang Padang".endswith("Padang")
print("ends = ", cek_ends)

# Penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'kamu']
gabung = ' '.join(pisah)
print(pisah)
print(gabung)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

# Alokasi karakter rjust(), ljust(), center()
print(5*"=" + "data" + "="*5)

kanan = " kanan ".rjust(20,"=")
print("'" + kanan +  "'")

kiri = " kiri ".ljust(20,"=")
print("'" + kiri +  "'")

tengah = " tengah ".center(20,"=")
print("'" + tengah +  "'")

# Kebalikannya ==> strip()
tengah = tengah.strip("=")
print("'" + tengah +  "'")