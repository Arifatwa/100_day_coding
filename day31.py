# mengkonvers menjadi list
data_range = range(1,10)
print(data_range)
data_range = list(data_range)
print(data_range)
print("=====================>\n")

# alternatif membuat list
data_range = range(1,10,2)
print(data_range)
data_range = list(data_range)
print(data_range)
print("=====================>\n")

# list menggunakan for 
pake_for = [i for i in range(0,10)]
print(pake_for)
print("=====================>\n")

list_pake_for = [i**2 for i in range(0,10)] # menggunakan kuadrat
print(list_pake_for)
print("=====================>\n")

list_pake_for_if = [ i for i in range(0,10) if i !=5]
# angka lima akan hilang
print(list_pake_for_if)
print("=====================>\n")

# menampilkan yang genap
list_pake_for_if = [ i for i in range(0,10) if i%2 ==0]
print(list_pake_for_if)
print("=====================>\n")

# menampilkan yang ganjil
list_pake_for_if = [ i for i in range(0,10) if i%2 !=0]
print(list_pake_for_if)