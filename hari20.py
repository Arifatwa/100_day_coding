#recursive, memanggil dirinya sendiri kembali

def belajar():
    pilihan = input("Masukkan hari pilihan anda : ")
    '''
    1. senin
    2. selasa
    3. rabu 
    4. kamis
    5. jum'at
    6. sabtu
    7. minggu
    '''

    if pilihan == "senin":
        print("Selalu ingin bersamamu\n")
        kembali = input("ketikkan y jika lanjut, n jika tidak: ")
        if kembali == "y":
            belajar() #recursive
        else :
            return
    elif pilihan == "selasa":
        print("Segalanya hanya untuk kamu saja\n")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar() #recursive
        else :
            return
    elif pilihan == "rabu":
        print("Rela berkorban untukmu\n")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar() #recursive
        else :
            return
    elif pilihan == "kamis":
        print("Kamu sangat manis hari ini\n")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar() #recursive
        else :
            return
    elif pilihan == "jum\'at":
        print("Jangan kamau tinggalkan aku\n")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar() #recursive
        else :
            return
    elif pilihan == "sabtu":
        print("Sangat indah waktu bersamamu\n")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar() #recursive
        else :
            return
    elif pilihan == "minggu":
        print("Mengingatmu adalah tugasku sepanjang waktu\n")
        kembali = input("ketikkan y jika lanjut, jika tidak : ")
        if kembali == "y":
            belajar() #recursive
        else :
            return
    else :
        print("Maaf pilihan anda tidak di temukan\n")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar() #recursive
        else :
            return
        
belajar()

    