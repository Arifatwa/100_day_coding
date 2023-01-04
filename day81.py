# TRy and except

while(True):
    angka = int(input("masukkan angka: "))
    try:
        hasil = 10 / angka
        print(f"hasil = {hasil}")
        is_done = input("lanjutkan (y/n)?")
        if is_done == "n":
            break
    except:
        print(f"pembagi nol, silahkan masukkan input lagi")


