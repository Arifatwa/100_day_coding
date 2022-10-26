# operasi logika atau boolean
# not , or, and, xor

# not
print("==========NOT=======")
a = True
c = not a 
print("data boolean = ", a)

print("_______________NOT")
print("data boolean = ", c)

# or, jika sala satu hasilnya adalh true maka hasilnya adalh true
print("==========OR=======")
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)
a = False
b = True
c = a or b
print(a, "OR", b, "=", c)
a = True
b = False
c = a or b
print(a, "OR", b, "=", c)
a = True
b = True
c = a or b
print(a, "OR", b, "=", c)

# AND, JIKA DUA BUAH NILAI TRUE MAKA AKAN TRUE
print("==========AND=======")
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)
a = False
b = True
c = a and b
print(a, "AND", b, "=", c)
a = True
b = False
c = a and b
print(a, "AND", b, "=", c)
a = True
b = True
c = a and b
print(a, "AND", b, "=", c)

# XOR, akan true jika sala satunya true maka akan true
print("==========XOR=======")
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
a = False
b = True
c = a ^ b
print(a, "XOR", b, "=", c)
a = True
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
a = True
b = True
c = a ^ b
print(a, "XOR", b, "=", c)

 