# operator komparasi 
# setiap hasil dari komparasi adalah boolean atau true dan false
# >, <, >=, <=, ==, !=, is, is not

x = 5
y = 4

# lebih besar dari > 
hasil = x > 4
print(x, ">", 4, "=", hasil )
hasil = y > 4 
print(y, ">", 4, "=", hasil )
hasil = x > y 
print(x, ">", 5, "=", hasil )
print("________________________")

# kurang dari <
hasil = x < 4
print(x, "<", 4, "=", hasil )
hasil = y < 4 
print(y, "<", 4, "=", hasil )
hasil = x < y 
print(x, "<", 5, "=", hasil )
print("________________________")

# besar dari sama dengan >=
hasil = x >= 4
print(x, ">=", 4, "=", hasil )
hasil = y >= 4 
print(y, ">=", 4, "=", hasil )
hasil = x >= y 
print(x, ">=", 5, "=", hasil )
print("________________________")

# kurang dari sama dengan <=
hasil = x <= 4
print(x, "<=", 4, "=", hasil )
hasil = y <= 4 
print(y, "<=", 4, "=", hasil )
hasil = x <= y 
print(x, "<=", 5, "=", hasil )
print("________________________")

# sama dengan
hasil = x == 4
print(x, "==", 4, "=", hasil )
hasil = y == 4 
print(y, "==", 4, "=", hasil )
print("________________________")

# tidak sam dengan !=
hasil = x != 4
print(x, "!=", 4, "=", hasil )
hasil = y != 4 
print(y, "!=", 4, "=", hasil )
print("________________________")

# is sebgai komparsi objek
a = 5 
b = 5
hasil = a is b
print("a is b ", hasil)
hasil = a is 5
print("a is 5 ", hasil)
print("________________________")

a = 5 
b = 5
hasil = a is not b
print("a is not b ", hasil)
hasil = a is not 4
print("a is not 5 ", hasil)
print("________________________")





