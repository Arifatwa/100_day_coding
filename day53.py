#menghitung akar kuadrat
#memasukan inputan angka
angka = float(input('Tuliskan Angka: '))
akar_kuadrat = angka ** 0.5
print('akar kuadarat dari %0.3f adalah %0.3f'%(angka,akar_kuadrat))
print("=====================================================")

#menyelesaikan persamaan kuadrat ax**2 + bx + c = 0
#mengimport modul cmath
import cmath
#menghitung angka 
a = int(input('Tulis a: '))
b = int(input('Tulis b: '))
c = int(input('Tulis c: '))

#mennghitung Diskriminan
d = (b**2) - (4*a*c)
x1 = (-b-cmath.sqrt(d))/(2*a)
x2 = (-b-cmath.sqrt(d))/(2*a)
#menampilkan hasil x1 dan x2
print('Hasil persaman kuadrat adalah {0} dan {1}'.format(x1,x2))