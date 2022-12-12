bil1 = input('Masukkan bilangan pertama: ')
bil2 = input('Masukkan bilangan kedua: ')

# Menjumlahkan bilangan
jumlah = float(bil1) + float(bil2)

# Menampilkan jumlah
print('Jumlah {0} + {1} adalah {2}'.format(bil1, bil2, jumlah))

print("==========Volume Prisma Segitiga=============")

tinggi_prisma = int(input("Tinggi Prisma : "))

alas_segitiga = int(input("Alas Segitiga : "))

tinggi_segitiga = int(input("Tinggi Segitiga : "))

volume = ( 1/2 * alas_segitiga * tinggi_segitiga ) * tinggi_prisma

print("Volume Prisma : %.0f" % (volume))