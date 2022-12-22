# keas kucing sebagai "definisi"
class kucing:
    warna = None
    usia = None

# membangun intence/variabel sebagai "objek nyata"
kucing1 = kucing()
kucing1.warna = "cokelat"
kucing1.usia = "1 tahun"

kucing2 = kucing()
kucing2.warna = "kuning"
kucing2.usia = "2 bulan"

kucing3 = kucing()
kucing3.warna = "hitam"
kucing3.usia = "4 bulan"

# memanggil atribut 
print("\n=============================")
print(kucing1.warna, kucing1.usia)
print(kucing2.warna, kucing1.usia)
print(kucing3.warna, kucing1.usia)

print("===============================================")
class mahasiswa:
    nama = None
    asal = None

    def perkenalan(self):
        print(f"perkenalkan saya {self.nama} dari {self.asal}")

arif = mahasiswa()
arif.nama = "MUH.ARIFATWA"
arif.asal = "MAMBI"

fisah = mahasiswa()
fisah.nama = "NURWAFISAH"
fisah.asal = "MAMBI"

arif.perkenalan()
fisah.perkenalan()
print("Nama : ", fisah.nama, ",", "Asal : ", fisah.asal)
print("Nama : ", arif.nama, ",", "Asal : ", arif.asal)





