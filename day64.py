class Buah:
    pass
buah_a = Buah()
buah_b = Buah()
buah_c = Buah();

buah_a.name = "Anggur"
buah_a.health = 20

buah_b.name = "Jeruk"
buah_b.number = 50

buah_c.name = "Melon"
buah_c.health = 70


print(buah_a)
print(buah_a.__dict__)

print(buah_b)
print(buah_b.__dict__)

print(buah_c)
print(buah_c.__dict__)
