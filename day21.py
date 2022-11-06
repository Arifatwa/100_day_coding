def kakulator():
    print("=========== KAKULATOR ===========")

    #operator +, -, *, /, %, **

    operator = input("Masukkan operator : ")
    angka1 = int(input("Masukkan angka1 : "))
    angka2 = int(input("Masukkan angka2 : "))

    if operator == "+": # penjumlahan
        hasil = angka1 + angka2
        print(angka1, "+", angka2, "=", hasil)
        kembali = input("ketikkan y jika lanjut, n jika tidak: ")
        if kembali == "y":
            kakulator() 
        else :
            return
    elif operator == "-": # pengurangan
        hasil = angka1 - angka2
        print(angka1, "-", angka2, "=", hasil)
        kembali = input("ketikkan y jika lanjut, n jika tidak: ")
        if kembali == "y":
            kakulator()           
        else :
            return
    elif operator == "*": # perkalian
        hasil = angka1 * angka2
        print(angka1, "x", angka2, "=", hasil) 
        pilihan = input("ketikkan y jika lanjut, n jika tidak: ")
        if pilihan == "y":
            kakulator()
        else :
            return
    elif operator == "/": # pembagiab
        hasil = angka1 / angka2
        print(angka1, "/", angka2, "=", hasil)
        kembali = input("ketikkan y jika lanjut, n jika tidak: ")
        if kembali == "y":
            kakulator() 
        else :
            return
    elif operator == "%": # sisa bagi
        hasil = angka1 % angka2
        print(angka1, "%", angka2, "=", hasil)
        kembali = input("ketikkan y jika lanjut, n jika tidak: ")
        if kembali == "y":
            kakulator() 
        else :
            return
    elif operator == "**": # sisa bagi
        hasil = angka1 ** angka2
        print(angka1, "**", angka2, "=", hasil)
        kembali = input("ketikkan y jika lanjut, n jika tidak: ")
        if kembali == "y":
            kakulator() 
        else :
            return
    else:
        print("Maaf operator yng anda masukkan salah")
        kembali = input("ketikkan y jika lanjut, n jika tidak: ")
        if kembali == "y":
            kakulator() 
        else :
            return

kakulator()