s = float(input("Masukan sisi persegi / Bujur sangkar:"))
luas = s*s
print("Luas Persegi / Bujur sangkar adalah :",luas)

m = input("Masukan jumlah baris:")
n = input("Masukan jumlah kolom:")
x = [s]*m
for i in range(m):
    x[i] = [1]*n
    print (x)