nama = input("Nama karyawan : ")
golongan = input("Masukkan golongan (1/2/3) : ")
lama_Kerja = int(input("Lama tahun kerja : "))

print(f"Nama karyawan : {nama}")
print(f"golongan : {golongan}")

# gaji pokok berdasarkan golongan
if golongan == "1":
    gaji = 4000000
    print(f"gaji_pokok : {gaji}")
elif golongan == "2":
    gaji = 7000000
    print(f"gaji_pokok : {gaji}")
elif golongan == "3":
    gaji = 10000000
    print(f"gaji_pokok : {gaji}")
else :
    print("Golongan tidak di temukan")

# bonus gaji
if lama_Kerja > 5 :
    bonus = lama_Kerja * 100000
else :
    bonus = 0

print(f"Bonus : {bonus}")
print(f"Gaji bersih : {gaji + bonus}")


