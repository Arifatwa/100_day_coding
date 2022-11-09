def li():
    nim = [1,2,3,4,5,6,7]
    for i in nim:
        if i % 2 == 0:
            print(i,"=", "genap")
        else:
            print(i,"=", "ganji")
li()
print("==============================\n")

def jual():
    menu = ["es kopi",
            "es teh",
            "es cincau",
            "es mantan"]

    print("menu Kami =", menu)
    piliahan = input("masukkan menu : ")
    if piliahan in menu:
        print("YAH, MENU SIAP, SILAHKAN DI TUNGGU")
    else:
        print("MAAF, MENU YANG ANDA PESAN TIDAK TERSEDIA DI DAFTAR MENU")
        perintah = input("ketikkan y untuk pilih menu, n jika tidak")
        if perintah == "y":
            jual()
        else:
            return
jual()
    