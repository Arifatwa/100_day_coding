
# contoh kasus


# contoh kasus

gaji = int(input("Masukkan gaji anda : "))
pekerjaan = input("Masukkan pekerjaan anda : ".lower())

if gaji >= 10000000 and pekerjaan == "pns":
    pajak = gaji * 5 / 100
    print(f"pajak = {pajak}")
    print(f"gaji bersih = { gaji - pajak}")

elif gaji >= 20000000 and pekerjaan == "pns":
    pajak = gaji * 8 / 100
    print(f"pajak = {pajak}")
    print(f"gaji bersih = { gaji - pajak}")

elif gaji >= 10000000:
    pajak = gaji * 2 / 100
    print(f"pajak = {pajak}")
    print(f"gaji bersih = { gaji - pajak}")

elif gaji >= 20000000:
    pajak = gaji * 5 / 100
    print(f"pajak = {pajak}")
    print(f"gaji bersih = { gaji - pajak}")

elif pekerjaan == "pns":
    pajak = gaji * 3 / 100
    print(f"pajak = {pajak}")
    print(f"gaji bersih = { gaji - pajak}")

else :
    pajak = 0
    print(f"pajak = {pajak}")
    print(f"gaji bersih = { gaji - pajak}")
<<<<<<< HEAD






=======
    
# mohon di terima {'-'}
>>>>>>> 2f64899fb7076dd97d9ab1853c3fa7c0f6cf3d16
