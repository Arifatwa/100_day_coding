# input user & cating 
# type data string
nama = input(" masukkan nama anda : ") # menggunakan kata kunci input 
print("nama anda adalah : ", nama)
print("nama anda adalah : ", nama , "bertype data : ", type(nama)) # untuk melihat type data yg di pakai

# type data integer & float
nilai = int(input("masukkan nilai anda : ")) # mengunakan casting
nilai = float(input("Masukkan nilai float : "))
print("Nilai anda adalah : ", nilai)
print("Nilai anda adalah : ", nilai , "bertype data : ", type(nilai))

# bolean 
nilai_bool  = bool(int(input("masukkan nila boolean : "))) # 0 = false , 1 = true
print("Nilai anda adalah : ", nilai_bool)
print("Nilai anda adalah : ", nilai_bool , "bertype data : ", type(nilai_bool))

