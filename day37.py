# contoh kasus

gaji = int(input("Masukkan gaji anda : "))
pekerjaan = input("Masukkan pekerjaan anda : ")

if gaji >= 10000000 and gaji <= 20000000 and pekerjaan == "pns".lower():
    pajak = gaji / (5 % 100)
    print(f"Pajak = {pajak}")
elif gaji >= 20000000 and pekerjaan == "pns".lower():
    pajak = gaji / (8 % 100)
    print(f"Pajak = {pajak}")
elif gaji <= 10000000 and pekerjaan == "petani" or "buruh" or "pengangguran".lower():
    pajak = 0
    print(f"Pajak = {pajak} %")
else :
    print("TIDAK DI KENAKAN PAJAK")
 

