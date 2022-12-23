class mahasiswa:
    pass

mahasiswa1 = mahasiswa()
mahasiswa2 = mahasiswa()

mahasiswa1.nama = "ARIFATWA"
mahasiswa1.umur = 19

mahasiswa2.nama = "ADRIAWAN"
mahasiswa2.umur = 19


print(mahasiswa1.__dict__)
print(mahasiswa2.__dict__)
print("Nama :",mahasiswa1.nama, "Umur :", mahasiswa1.umur)
print("Nama :",mahasiswa2.nama, "Umur :", mahasiswa2.umur)