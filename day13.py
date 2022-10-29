password = "arif"
n = 1
while n < 5:
    n += 1
    input_password = input("Masukkan Password : ")
    if input_password == password:
        print("Berhasil login")
        break
    else:
        print("Password yang anda masukkan salah")
        continue
    if n == 5:
        print("Gagal Login")
        break