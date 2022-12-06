#Menginput Sisi Kubus
sisi = float(input('Tulis sisi Kubus:'))
#Menghitung Volume Kubus
volume = sisi**3
#Menampilkan Hasil perhitungan
print('Volume Kubus adalah %0.2f' %volume)

#Menginput Tahun
tahun = int(input("Tulis Sebuah Tahun: "))

#Perulangan Pertama
if (tahun % 4) == 0:

   #Perulangan Kedua
   if (tahun % 100) == 0:

       #Perulangan Ketiga
       if (tahun % 400) == 0:

           #Tergolong Tahun Kabisat
           print("{0} adalah Tahun Kabisat".format(tahun))

       #Bukan Tergolong Tahun Kabisat
       else:
           print("{0} bukan Tahun Kabisat".format(tahun))

   #Tergolong Tahun Kabisat
   else:
       print("{0} adalah Tahun Kabisat".format(tahun))

#Bukan Tergolong Tahun Kabisat
else:
   print("{0} bukan Tahun Kabisat".format(tahun))
