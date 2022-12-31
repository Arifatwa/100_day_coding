'''
program yang dapat menerima imputan angka dengan ketentuan 
1. angka yang di masukkan melalui input adalah batas atas angka
2. program menampilkan jumlah angka yang habis di bagi 3
contoh angka yang di input adalah 10, maka jawabannya adalah 3
karna ada 3 angka yang habis di bagi 3 yaitu 3, 6, dan 9
'''

angka = int(input("masukkan angka :"))
n = angka // 3
print(n)