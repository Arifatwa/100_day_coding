gaji = int(input("Masukan Gaji perbulan:"))
if gaji >= 15000000 and gaji < 25000000:
    pajak = 2/100
    total_pajak = pajak*gaji
    gaji_bersih = gaji-total_pajak
elif gaji >= 25000000:
    pajak =5/100
    total_pajak = pajak*gaji
    gaji_bersih = gaji-total_pajak
elif gaji < 15000000:
    gaji_bersih = gaji

print("Total Gaji bersih : Rp.",gaji_bersih)