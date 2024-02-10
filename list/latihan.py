# Program list buku

list_buku = []
while True:
    print("\n===== MASUKAN DATA BUKU =====")
    judul = input("\nMasukan Judul buku \t= ")
    penulis = input("Masukan Penulis buku \t= ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)
    
    print("\nNo.\t| Judul \t | Penulis")
    for index,buku in enumerate (list_buku):
        print(f"{index+1}\t| {buku[0]} \t | {buku[1]}")
    
    print("\n","="*20)
    isLanjut = input("Apakah di lanjutkan? (y/n) =")

    if isLanjut == "n":
        break
print("Program Selesai")