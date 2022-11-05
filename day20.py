#recursive

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
            belajar()
        else :
            return
    elif pilihan == "selasa":
        print("Segalanya hanya untuk kamu saja")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar()
        else :
            return
    elif pilihan == "rabu":
        print("Rela berkorban untukmu")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar()
        else :
            return
    elif pilihan == "kamis":
        print("Kamu sangat manis hari ini")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar()
        else :
            return
    elif pilihan == "jum\'at":
        print("Jangan kamau tinggalkan aku")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar()
        else :
            return
    elif pilihan == "sabtu":
        print("Sangat indah waktu bersamamu")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar()
        else :
            return
    elif pilihan == "minggu":
        print("Mengingatmu adalah tugasku sepanjang waktu")
        kembali = input("ketikkan y jika lanjut, jika tidak : ")
        if kembali == "y":
            belajar()
        else :
            return
    else :
        print("Maaf pilihan anda tidak di temukan")
        kembali = input("ketikkan y jika lanjut, n jika tidak : ")
        if kembali == "y":
            belajar()
        else :
            return
        
belajar()

    