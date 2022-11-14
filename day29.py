# belajar List ----> nested list / list bersarang

mahasiswa_1 = ["Arif",19,"Takurimbik","laki-laki"]
mahasiswa_2 = ["fisah",20,"lombongang","wanita"]
mahasiswa_3 = ["adriawan",21,"bambang","laki-laki"]
mahasiswa_4 = ["alim",22,"timbaang","laki-laki"]

list_mahasiswa = [mahasiswa_1,
                  mahasiswa_2,
                  mahasiswa_3,
                  mahasiswa_4]
print(f"Mahasiswa{list_mahasiswa}")

for mahasiwa in list_mahasiswa:
    print(f"Nama\t: {mahasiwa[0]}")
    print(f"Umur\t: {mahasiwa[1]}")
    print(f"Alamat\t: {mahasiwa[2]}")
    print(f"jenis kelamin\t: {mahasiwa[3]}\n")