# belajar args dan kwargs

# args
print("++++++++++++++*Args+++++++++++++\n")

def nama(*args): # untuk kata argsnya boleh kata lain, tidak mslh 
    n = 0
    for i in args:
        n += 1
        print(str(n)+". "+ i)
nama("Arifatwa","Fisah","Ahmad","Alim", "dll")



print("++++++++++++++**Kwargs+++++++++++++\n")
# kwargs
def name(**kwargs):
    for k,v in kwargs.items():
        print(k, ":", v)

name(Arif = "90", Fisah = "80", Ahmad = 70, Alim = "60", sampai = "sebanyak banyaknya")



print("+++++++++++++++++++++++++++++++++++\n")
# tambahan
# bisa di tambah lagi, dengan cara memanggil funsinya, and masukkan velue
nama("Arifatwa","Fisah","Ahmad","Alim", "dll", "tambah lagi")
print("+++++++++++++++++++++++++++++++++++\n")
name(Arif = "90", Fisah = "80", Ahmad = 70, Alim = "60", sampai = "sebanyak banyaknya", tambah = "lagi")



