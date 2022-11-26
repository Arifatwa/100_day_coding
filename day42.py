#Ruang lingkup (dan siklus hidup) variabel pada fungsi
#variabel global
#adalah variabel  yang bisa di panggil dari manapun dari file phyton
#variabel lokal
#adalah variabel yang hanya hidup di dalam satu blok kode tertentu (seperti di dalam fungsi)

Buah = 'Melon'

def manisnya():
    print(Buah)

print('print secara langsung enaknya buah', Buah)
print('[panggil fungsi manisnya buah]', end=' ')
manisnya()
print("\n===================================================")

kota, provinsi = 'Sulbar', 'sulsel'
def hello ():
    provinsi = 'Sulbar'
    print(kota, provinsi)
    
print('[PANGGIL FUNGSI hello()]')
hello()
print('\n[SECARA LANGSUNG]')
print(kota, provinsi)
