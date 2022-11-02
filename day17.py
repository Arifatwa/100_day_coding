# oop dasar 
class manusia(): # objek (manusia)
    def __init__(self,nama,umur,tinggi,status): # atribut ( nama, dll)
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggi
        self.status = status

        # method 
    def makan(self):
        print("Saya makan : makan nasik, sayur, dan ikan")
    def jalan(self):
        print("Saya jalan : pakai sandal dan melangkah")
    def suara(self):
        print("Suara saya : Berteriak dan tertawa")


# objek
objku = manusia("Arifatwa", 19, 70.5, "mahasiswa")
# cara pemanggilan objek
print("--------------------------------\n")
print("Nama saya adalah :", objku.nama)
print("Umur saya :", objku.umur)
print("Tinggi :", objku.tinggi)
print("Status :", objku.status)
print("--------------------------------\n")
# cara pemanggilan method
objku.makan()
objku.jalan()
objku.suara()
