# memanipulasi data list
data = ["arifatwa", "adriawan", "alim", "hendara"]
print("data = ",data)

# mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_arifatwa = data[-4]
print(f"data arif = {data_arifatwa}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}\n")


print("------------> manipulasi data list")
# menambah
print(f"data sebelum di tambah = {data}\n")
data.insert(1,"fisah")
print(f"data yang di tambah = {data}\n")

# menambahkan di akhir list
data.append("ahmad")
print(f"data di tambah = {data}\n")

# menambahlkan list dengan list
data_baru = ["naruto", "sasuke", "sakura", "hinata"]
print("data baru = ",data_baru,"\n")
data.extend(data_baru)
print(f"data gabungan  = {data}\n")

# merubag data 
# mengubah data 
data[4] = "itachi"
print(f"data rubah = {data}\n")

# menghapus data 
data.remove("adriawan")
print(f"data remove = {data}\n")

# menghapus data paling belakang
data.pop()
print(f"data ahkir = {data}")



