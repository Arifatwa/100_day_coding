print("Harga diamond = 12.000".center)
jumlah_paket = int(input("Masukkan jumlah paket yang akan di beli: "))
harga_perpaket = 120000
harga_total_paket = jumlah_paket*harga_perpaket

if(jumlah_paket >= 10 and jumlah_paket <= 19):
    diskon = 20/100
elif(jumlah_paket >= 20 and jumlah_paket <= 49):
    diskon = 30/100
elif(jumlah_paket >= 50 and jumlah_paket <= 69):
    diskon = 35/100
elif(jumlah_paket >= 70 and jumlah_paket <= 99):
    diskon = 40/100
elif(jumlah_paket >= 100):
    diskon = 50/100
else:
    diskon = 0

jml_diskon = harga_total_paket * diskon
jum_harga_setelah_diskon = harga_total_paket - jml_diskon

print(f"Haga per paket : Rp.{harga_perpaket}")
print(f"Harga total paket: Rp.{harga_total_paket}")
print(f"Harga total setetlah diskon: Rp.{jum_harga_setelah_diskon}")
print(f"jumlah uang yang di hemat: Rp.{jml_diskon}")
