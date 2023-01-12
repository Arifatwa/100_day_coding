barang = input("Masukkan jenis barang /A/B/C : ")
harga = int(input("Harga barang : "))


if barang == "A":
    diskon_A = 10/100
    harga_Sebelum_diskon = harga * diskon_A
    Total_harga_setelah_diskon = harga - harga_Sebelum_diskon
    print("jenis barang yang di pilih : " , barang) 
    print("harga sebelum diskon       : " , harga_Sebelum_diskon) 
    print("Total harga setelah diskon : " , Total_harga_setelah_diskon) 
elif barang == "B":
    diskon_B = 15/100
    harga_Sebelum_diskon = harga * diskon_B
    Total_harga_setelah_diskon = harga * harga_Sebelum_diskon
    print("jenis barang yang di pilih : " , barang) 
    print("harga sebelum diskon       : " , harga_Sebelum_diskon) 
    print("total harga setelah diskon : " , Total_harga_setelah_diskon) 
elif barang == "C":
    diskon_C = 20/100
    harga_Sebelum_diskon = harga * diskon_C
    total_harga_setelah_diskon = harga - harga_Sebelum_diskon
    print("jenis barang yang di pilih : " , barang) 
    print("harga sebelum diskon       : " , harga_Sebelum_diskon) 
    print("total harga setelah diskon : " , total_harga_setelah_diskon) 
else :
    print("coba lagi")