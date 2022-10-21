# operasi aritmatika

nilai1 = 10
nilai2 = 4

# tambah 
hasil = nilai1 + nilai2 
print(nilai1, "+", nilai2, "=", hasil)

# kurang
hasil = nilai1 - nilai2 
print(nilai1, "-", nilai2, "=", hasil)

# kali 
hasil = nilai1 * nilai2 
print(nilai1, "*", nilai2, "=", hasil)

# bagi 
hasil = nilai1 / nilai2 
print(nilai1, "/", nilai2, "=", hasil)

# pangkat 
hasil = nilai1 ** nilai2 
print(nilai1, "**", nilai2, "=", hasil)

# modulus atau sia bagi
hasil = nilai1 % nilai2 
print(nilai1, "%", nilai2, "=", hasil)

# floor division atau pembulatan float
hasil = nilai1 // nilai2 
print(nilai1, "//", nilai2, "=", hasil)


# prioritasa operasi , oprarationl precedence 
'''
1 . ( )    
2. eksponen
3. perkalian * % // **
4. penjumlahan + - 

'''
x = 5
y = 4
z = 2

hasil = x * y + z - y // x % z ** y
print(x, "*", y, "+", z ,"-", y, "//", x, "%", z, "**", y, "=", hasil)

# dalam kurung akan di dahulukan
hasil = x * y + (z - y) // x % z ** y
print( x, "*", y, "+", "(", z ,"-", y, ")", "//", x, "%", z, "**", y, "=", hasil)


