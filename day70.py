class Buah:
    nama = None
    warna = None

    def namanya(self):
        print(f'namanya buah {self.nama} dan  buah ini berwarna {self.warna}')


buah = Buah()
buah.nama = "Jeruk"
buah.warna = "Orange"

buah_a = Buah()
buah_a.nama = "Apel"
buah_a.warna = "merah"

buah.namanya()
buah_a.namanya()