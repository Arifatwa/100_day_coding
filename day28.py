# mengisi velue dictionary dengan inputan user

template_mahasiswa = {
        "nama":" ",
        "nim":" ",
        "sks_lulus":0,
        "status":" "
}

data_mahasiswa = {}
mahasiswa = dict.fromkeys(template_mahasiswa.keys())
print("Mahasiswa =", mahasiswa,"\n") # dict tanpa key(nilai)
mahasiswa["nama"] = input("Nama saya : ")
print("Mahasiswa =", mahasiswa,"\n")
mahasiswa["nim"] = input("Nim mahasiswa : ")
print("Mahasiswa =", mahasiswa,"\n")
mahasiswa["sks_lulus"] = input("sks mahasiswa : ")
print("Mahasiswa =", mahasiswa,"\n")
mahasiswa["status"] = input("status mahasiswa : ")
print("Mahasiswa =", mahasiswa,"\n")