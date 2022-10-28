# belajar list

li = ["arifatwa","fisah","ahmad","adriawan"]
isi = input("Masukkan isi dalam list : ")

li.append(isi) # menambahkan list
li.insert(1,input("Masukkan isi : ")) # menyisipkan nilai pada list
del li[int(input("masukkan indek yang akan di hapus : "))] # menhapus list
li.pop(int(input("masukkan indeks yang akan di hapus : "))) # menhapus dengan list

print(li)