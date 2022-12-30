'''
1. jika yang di masukkan angka genap maka akan 
    menampilkan pesan genap dan akan meminta angka lagi
2. jika yang di masukkan angak ganjil maka akan menampilkan pesan
    you and i, and
'''
def kondisi():
    angka = int(input("Masukkan angka :"))
    while True:
        if angka % 2 == 0:
            print("genap")
            kondisi()
        elif angka % 1 == 0:
            print("You and i, and")
        break
kondisi()