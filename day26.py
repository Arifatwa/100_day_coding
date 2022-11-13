# belajar perulangan 
angka = int(input("Masukkan angka : "))
for i in range (1, angka+1):  
    print(i*"*")

print("=========================")

i = 0
for i in range(1,11): # akan mengeluarkan output 1 - 10
    print(i)

print("=========================")

i = 0
for i in range(1,10, 2): # akan mengelluarkan output kelipatan dari 2 1 - 10
    print(i)

#BELAJAR PERULANGAN dengan memmberikan kodisi

print("===================================")
# menghasilkan 1,2 3
nomor = 1
while True:
        print(nomor)
        nomor += 1
        if nomor >= 5:
                break

print("===================================")
# menghasilkan bilangan genap di bwah 15
for i in range(15):
        if i % 2 == 1:
                continue
        print(i)



