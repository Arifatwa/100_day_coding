nama = input("Nama karyawan :")
gaji = int(input("Gaji pokok :"))
jml_anak = int(input("Jumlah anak :"))
status_Nikah = input("Status Nikah y / n :".lower())

print(f"\nNama karyawan = {nama}")
print(f"gaji poko = {gaji}")

tunjangan_anak = jml_anak * (gaji * 5 / 100)
print(f"Tunjangan anak = {tunjangan_anak}")
if status_Nikah == "Y":
    tunjangan_istri = gaji * 2 / 100
    print(f"tunjangan istri = {tunjangan_istri}")
else :
    tunjangan_istri = 0
    print(f"tunjangan istri = {tunjangan_istri}")

gaji_awal = tunjangan_anak + gaji + tunjangan_istri
pajak = gaji_awal * 10 / 100
gajiBersih = gaji_awal - pajak

print("\n====================================\n")

print(f"jumlah tunjangan = {tunjangan_istri + tunjangan_anak}")
print(f"gaji pokok = {gaji_awal}")
print(f"Total pajak = {pajak}")
print(f"gaji bersih = {gajiBersih}\n")