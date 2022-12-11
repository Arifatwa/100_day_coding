total = 100000
setelah_diskon = total

if total < 200000:
    diskon = total * (7/100)
else:
    diskon = total * (20/100)

setelah_diskon = total - diskon
print('diskonya yaitu : {}'.format(int(diskon)))
print('Harga setelah diskon : {}'.format(int(setelah_diskon)))