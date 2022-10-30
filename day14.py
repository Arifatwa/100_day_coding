# data and time (latihan)
import datetime as dt


hari_ini = dt.date.today()
print('Data hari ini :',hari_ini)
print(f"hari ini adalah hari : {hari_ini:%A}")
print("=======")

tgl = dt.date(2003,10,25)
print("data saya : ", tgl)
print(f"hari ini adalah hari : {tgl:%A}")
print("========================================")


# latihan
print("=MEMBUAT KAKULATOR TANGGAL LAHIR=")
tanggal = int(input("Masukkan tanggal \t: "))
bulan = int(input("Masukkan bulan \t\t: "))
tahun = int(input("Masukkan tahun \t\t: "))

print("=========HASIL DATA ===========")
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"hari lahirnya adalah : {tanggal_lahir:%A}")
umur_hari = hari_ini - tanggal_lahir
print(umur_hari)
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30

print(f"Umur anda adalah : {umur_tahun} tahun, {umur_bulan} bulan " )
print(f"Data hari ini adalah : {hari_ini}")