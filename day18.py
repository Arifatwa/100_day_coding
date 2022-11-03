'''
inheritens, (sebuah kelas yang mewarisi properti
properi dari kelas lain, baik itu atribut maupun merhod

'''
class A :
    def __init__(self, umur, tinggi, status):
        self.umur = umur
        self.tinggi = tinggi
        self.status = status

class B(A): #inheritens
    nama = "arif"
    
    
C = B(19,170.3, True)
print(C.nama)
print('Umur :', C.umur)
print('Tinggi :',C.tinggi)
print('Mahasiswa : ', C.status)




