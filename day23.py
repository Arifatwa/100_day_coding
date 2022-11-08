# belajar nestid if ( if yang bertingkat-tingkat)

umur = int(input("Umur anda : "))
pendidikan = input("Pendidikan terakhir anda : ")

if umur >= 25 and umur <= 40:
    if pendidikan == "s1" or pendidikan == "s2" or pendidikan == "s3":
        print("selamat anda di terima di perusahaan kami")
else :
    print("maaf anda belum bisa kami terima")
