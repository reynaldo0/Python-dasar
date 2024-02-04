import datetime as dt

print("Silahkan masukan tanggal,\nbulan dan tahun lahir anda\n")
tanggal = int(input("Tanggal \t = "))
bulan = int(input("Bulan \t\t = "))
tahun = int(input("Tahun \t\t = "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda = {tanggal_lahir}")
print(f"Hari nya adalah hari = {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal = {hari_ini}")
umur = hari_ini - tanggal_lahir
umur_tahun = umur.days // 365
umur_bulan = (umur.days % 365) // 30
    
print(f"umur anda adalah  = {umur_tahun} Tahun, {umur_bulan} Bulan,  dan {umur}")
