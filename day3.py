# Belajar cesting. Merubah type data ke type data yang lain
print("________integer________")
data_int = 10
print("data : ", data_int,"type : ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_str)
print("data : ", data_float, "type : ", type(data_float))
print("data : ", data_str, "type : ", type(data_str))
print("data : ", data_bool, "type : ", type(data_bool))

print("________float________")
data_float = 9.0
print("data : ", data_float,"type : ", type(data_float))

data_int = int(data_float) # akan di bulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai float adalah nol
print("data : ", data_int, "type : ", type(data_float))
print("data : ", data_str, "type : ", type(data_str))
print("data : ", data_bool, "type : ", type(data_bool))

print("________boolean________")
data_bool = 0 # jika false. 1 jika true
print("data : ", data_bool,"type : ", type(data_bool))

data_int = int(data_bool) 
data_str = str(data_bool) # akan langsung di tulis 
data_float = bool(data_bool) 
print("data : ", data_int, "type : ", type(data_bool))
print("data : ", data_str, "type : ", type(data_bool))
print("data : ", data_float, "type : ", type(data_bool))

print("________string________")
data_str = "8"
print("data : ", data_str,"type : ", type(data_str))

data_int = int(data_str) # tidak bisa di konver ke int,
# kecuali stringnya di isi dengan angka
data_float = float(data_str)
data_bool = bool(data_str) 
print("data : ", data_int, "type : ", type(data_int))
print("data : ", data_float, "type : ", type(data_float))
print("data : ", data_bool, "type : ", type(data_bool))







