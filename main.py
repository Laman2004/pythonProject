book=["kitab","defter","qelem"]  # list
saylar=[1,5,7,9,8,0]
"""
print(book)
book.append("yonan")   # elave etmek
print(book)
book.insert(2,"pozan")    # indekse gore elave etmek
print(book)
book.extend(["silgi","xetkes"])   # list-i ayri elave etmek
print(book)
book.remove("defter")     # elementi silmek
print(book)
silinen=book.pop()     # sonuncu elementi silir
print(silinen)
print(book)
book.reverse()    # tersine ekrana cixarma
print(book)
print(sorted(book))       # siralayir ve listi deyismir
print(book)      # yuxaridaki ile eynidir))
book.sort()
print(book)     # siralayir ve listi deyisdirir
print(min(saylar))         # en kicik
print(min(book))       # en 1-ci element
print(max(saylar))     # en boyuk
print(max(book))       # en sonuncu
print(sum(saylar))     # cemini hesablamaq
print(list(enumerate(book)))  # indeksle listin elementlerini yazir
print(list(enumerate(saylar,start=3)))     # listin elementlerinin indeksi start-la baslayir
mesaj="-".join(book)     # listi stringe cevirir
print(mesaj)
print(mesaj.split("-"))    # stringi liste cevirir
if 5 > 2:
 print("Five is greater than two!")"""
 # tuple ve set ve dictionary
"""tpl=("ADNSU","ADU","BDU","BANM","AzTU")
print(tpl)
print(len(tpl))
setler={"insan","heyvan","nitq","Heserat"}
setler1={"insan","real","data","heyvan"}
print(setler)
setler.add("nitq")
print(setler)
# setler.remove("Heserat")
# setler.remove("kitab")  olmayan bir seyi silmeye calismaq ve sehv verecek)
# setler.discard("kitab")   sehv vermeyecek(
print(setler.intersection(setler1))
print(setler.union(setler1))
print(setler.difference(setler1))
print(setler1.difference(setler))
print(set("PYTHON"))
freelist=[]   # listdir
freelist1=list()
freetuple=()   # tuple-dir
freetuple1=tuple()
freeset=set()  # setdir
freeset1={}   # dictionary-dir
print(type(freelist),type(freelist1))
print(type(freetuple),type(freetuple1))
print(type(freeset),type(freeset1))"""
# dictionary
adam={"isim":"Laman","Soyisim":"Mikayilova","Yas":19,"Qrup":603.21}
print(adam)
print(type(adam))
print(adam["isim"])  # key-e gore value-ni ekrana yazir
adam["isim"]="Nazrin"  # keyin value-sini deyismek
adam["sinif"]="10L"      # yeni key ve value elave etmek
print(adam["isim"],adam["sinif"])
del(adam["Qrup"])     # silmek
adam.update({"isim":"Amin","Soyisim":"Mikayilov","sinif":4,"Yas":9})  # key ve value-ni deyismek
print(adam)
"""for i in adam:
 print(i)      #  key-leri ekrana cixarir"""
"""for i in adam:
  print(adam[i])      # value-leri ekrana cixarir
print(adam.keys())    # key-leri ekrana cixarir
print(adam.values())    # value-leri ekrana cixarir
print(adam.items())     # key ve value-leri ekrana cixarir
for i,j in adam.items():
 print(i,j)          # her ikisini ekrana cixarir"""
for i in adam.items():
  print(i)       # dirnaq icerisinde her ikisini ekrana cixarir
print(adam.get("isim"))   # axtarir ve sehv olarsa,sehvi gostermir
print(adam.get("ad","Laman"))



