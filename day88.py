total =int(input("masukkan total belanja anda  : Rp.  ")) 
setelah_diskon = total 

if total >= 90000:
    diskon = total * (3/100)
else:
    diskon = total * (10/100) 

setelah_diskon = total - diskon 

print("Diskonnya yaitu : {} " .format(int(diskon)))
print("harga setelah diskon : {} " .format(int(setelah_diskon))) 

# latihan membuat class dan objek 

class Handphone:
    pass 

hp1= Handphone()  



hp1.name = "VIVO Y20" 
hp1.ukuran = "ukuran : 6.51 INCI" 
hp1.color = "warna : Black" 

print("========CLASS DAN OBJEK========")
print(hp1.name) 
print(hp1.ukuran) 
print(hp1.color) 