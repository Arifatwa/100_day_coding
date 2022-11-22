gaji = int(input("Masukkan gaji anda : "))
jumlah_alfa = int(input("Masukkan Juamlah Alfa : "))

if jumlah_alfa > 5 :
    pajak = 25000 * jumlah_alfa
    gaji_bulanan = gaji - pajak
    potongan = gaji_bulanan * (2.5 / 100) 
    gaji_bersih = gaji_bulanan - potongan
    print(f"gaji bersih = {gaji_bersih}")
else :
    pajak = gaji * 2.5 / 100
    gaji_bersih = gaji - pajak
    print(f"Gaji bersih = {gaji_bersih}")

     
    

