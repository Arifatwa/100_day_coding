# penjumlahan
class bilangan():
    def __init__(self, angka1, angka2, angka3):
        self.angka1 = angka1
        self.angka2 = angka2
        self.angka3 = angka3

panggilan = bilangan(10,19,20)
print("Hasil :",panggilan.angka1 + panggilan.angka2)
print("Haisil :",panggilan.angka2 * panggilan.angka3)
print("Hasil :",panggilan.angka3 % panggilan.angka2)