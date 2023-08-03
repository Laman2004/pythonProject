"""f=open("test1","r")   # fayli acib oxumaq
inner=f.read()
print(inner)
f.close()"""            # fayli baglamak

"""with open("test1") as file:
    for satir in file:
        print(satir,end="")    # \n-leri yox etmek"""

"""with open("test1") as f:               # test1-deki yazini test2-e yazmaq
    with open("test2","w") as W:
        for satir in f:
            W.write(satir)"""

"""with open("test1") as file:
    f=file.readlines()             # ekrana list seklinde cixaracaq
    print(f)"""

"""with open("test1") as file:
    f=file.readline()              # 1 setiri ekrana cixarir
    print(f,end="")
    print(file.tell())             # imlecin yerini gosterir
    file.seek(0)                   # imlecin yerini deyisdirir
    f=file.readline()
    print(f,end="")
    f=file.readline()
    print(f,end="")"""

"""with open("test2","a") as wfile:    # file-a elave edir
    wfile.write("Azerbaijan  ")"""

"""with open("pythonpng.jpeg","rb") as f:
    with open("python.png","wb") as w:    # text tipinde olmayan fayllarla yazma ve oxuma
        for satir in f:
            w.write(satir)"""




