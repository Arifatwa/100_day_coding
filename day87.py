class mahasiswa:
    def __init__(self, nama, umur, status):
        self.nama = nama
        self.umur = umur
        self.status = status 
    #method
    def kelakuan(self):
        print("tidak bisa hidup tanpa bantuan orang lain")

class ARIFATWA(mahasiswa):
    def __init__(self, nama, umur, status):
        super().__init__(nama, umur, status)
    # method 
    def keahlian(self):
        print("saling memenbutuhkan bantuan antar sesama")
       

class wafisah(mahasiswa):
    def __init__(self, nama, umur, status, tinggi):
        super().__init__(nama, umur, status)
        self.tinggi = tinggi
    def keahlian(self):
        print("saling butuh kasih sayang hhh")

mahasiswa1 = ARIFATWA('Muh.Arifatwa', 19, "kuliah")
print("nama Lengkap ARIFATWA", mahasiswa1.nama)
print("umur ARIFATWA",mahasiswa1.umur, "tahun")
print("status ARIFATWA",mahasiswa1.status)
#pemanggilan method
mahasiswa1.kelakuan()
mahasiswa1.keahlian()
print("________________________________\n")

mahasiswa2 = wafisah("nurwafisah", 19, "kuliah", 50.3)
print(f"nama lengkap wafisah adalah {mahasiswa2.nama}")
print(f"umur wafisah {mahasiswa2.umur} tahun")
print(f"status wafisah {mahasiswa2.status}")
print(f"tinggi wafisah berukuran {mahasiswa2.tinggi} cm")
# pemanggilan method
mahasiswa2.kelakuan()
mahasiswa2.keahlian()
