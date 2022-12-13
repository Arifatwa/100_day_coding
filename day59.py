print("=======Menghitung kecepatan dan luas========")
def hitung_kecepatan():
    print('hitung kecepatan ready')
    jarak = float(input("masukan jarak:"))
    waktu = float(input("masukan waktu:"))
    kecepatan = jarak * waktu
    print("kecepatan: ", kecepatan,'\n')

def luas_segitiga():
    print("hitung luas segitiga :")
    alas = float(input("Masukan alas: "))
    tinggi = float(input("Masukan tinggi: "))
    luas = 0.5 *(alas * tinggi)
    print("luas segitiga adalah:", luas, "cm", "\n")

def luas_balok():
     print("hitung luas balok:")
     panjang = float(input("Masukan panjang: "))
     lebar = float(input("Masukan lebar:"))
     tinggi = float(input("Masukan tinggi:"))
     luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
     print("luas balok adalah: ", luas, "cm", "\n")

    
while True:
    userInput = int(input(
        "Pilih rumus yang akan di pakai: \n\n1.hitung kecepatan\n2.luas segitiga\n3.luas_balok\n\n0.keluar program\n\npilih nomor berapa: "))
        
    if(userInput == 1):
         hitung_kecepatan()
    elif(userInput == 2):
         luas_segitiga()
    elif(userInput == 3):
         luas_balok()
    
    else:
        break