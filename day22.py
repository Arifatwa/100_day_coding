def tipe_data():
    print("=========== TUPLE =============")
    tu = ("harimau", "singa", "macam", "naga")
    print(f"nilai = {tu}\n")
    #tu.append("gajah") # type data tuple tidak supor untuk di edit
    # baik di tambah maupun di kurang dari isi nya, jika di edit akan eror

    print("=========== LIST =============")
    li = ["arif", "fisah", "alim", "adriawan"]
    li.append("hendra") # menambah isi pada list
    del li[3] # menghapus 
    li.insert(2,"adriawan") #menyisipkan nilai
    print(f"nilai = {li}\n")

    print("=========== DICTYONARY =============")
    dic = {"arif":100, "fisah":90, "alim":80, "adriawan":70}
    dic["hendra"] = 23 # menambah
    del dic["arif"] # menghapus
    dic["fisah"] = 100 # mengganti nilai atau velue
    print(f"nilai = {dic}")
    for k,v in dic.items():
        print(k, ":", v,)

    print("=========== SET =============")
    se = {"arif", "fisah", 80, "adriawan"}
    #type data set tidak mengenal yg namanya index
    se.add("hendra") # menambah
    #del se[3] tidak dapat menghapus dengan index
    se.remove("arif") #menghapus
    print(f"nilai = {se}")
    


tipe_data()

