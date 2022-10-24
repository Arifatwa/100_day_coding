# latihan logika dan komparasi menggunakan input


inputuser = float(input("masukkan anhka yang bernilai di atas dari 5 atau kurang dari 10 : "))
# lebih dari 5
angka = (inputuser > 5)
print("lebih  dari 5 : ", angka)

# kurang dari 10 
angka2 = (inputuser < 10 )
print("kurang dari 10 : ", angka2)

hasil1 = angka or angka2
print("angka yang anda masukkan : ", hasil1)

inputuser = float(input("masukkan angka yang bernilai kurang 5 atau leih besar dari 10 : "))
angka = (inputuser < 5)
print("kurang dari 5 : ", angka)

angka2 = (inputuser > 10 )
print("lebih dari 10 : ", angka2)

hasil1 = angka and angka2
print("angka yang anda masukkan : ", hasil1)

