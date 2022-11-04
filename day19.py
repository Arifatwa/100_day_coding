'''
cara menggunakan kata super dalam inheritens di oop.
kelas super atau kelas turunan dari kelas induk.

'''

class binatangbuas:
    def __init__(self, umur, cakar, taring):
        self.umur = umur
        self.cakar = cakar
        self.taring = taring 
    #method
    def berlari(self):
        print("berlari dengan kawan")

class harimau(binatangbuas):
    def __init__(self, umur, cakar, taring):
        super().__init__(umur, cakar, taring)
    # method 
    def berburu(self):
        print("berburu sendiri")
       

class singa(binatangbuas):
    def __init__(self, umur, cakar, taring, surai):
        super().__init__(umur, cakar, taring)
        self.surai = surai
    def berburu(self):
        print("berburu dengan berkelompok")

arif = harimau(5, 4, 6)
print("umur harimau", arif.umur, "tahun")
print("cakar harimau",arif.cakar, "cm")
print("taring harimau",arif.taring, "cm")
#pemanggilan method
arif.berlari()
arif.berburu()
print("________________________________\n")

fisah = singa(8, 3, 4, 40)
print(f"umur singa adalah {fisah.umur} tahun")
print(f"panjang cakar singa {fisah.cakar} cm")
print(f"taring singa berukuran {fisah.taring} cm")
print(f"surai singa berukuran {fisah.surai} cm")
# pemanggilan method
fisah.berlari()
fisah.berburu()




