import os
from datetime import datetime

"""print(os.getcwd())
os.chdir("C:/Users/User-HP/PycharmProjects/pythonProject")
os.mkdir("C:/Users/User-HP/PycharmProjects/pythonProject/book")
for file in os.listdir():
    print(file)
os.makedirs("Python1/Python2/Python3")
for i,j,k in os.walk("C:/Users/User-HP/PycharmProjects/pythonProject/Python1"):
    print(f"Path: {i}")
    print(f"Folder: {j}")
    print(f"File: {k}")
    print("---------------------------------------------------------------------------------------------------------------")
print(os.path.isfile("Euler.py"))
print(os.path.isdir("Python3"))
print(os.path.splitext("sade_murekkeb_reqem.py"))
os.rename("book","kitab")
os.rmdir("kitab")
os.removedirs("Python1/Python2/Text3.txt")
for i,j,k in os.walk("C:/Users/User-HP/PycharmProjects/pythonProject/Python1/Python2"):
    print(i)
    print(j)
    print(k)
    print("****************************************************************************************************************")
os.remove("Text3.txt")"""
# file-lari uzantilarina gore folder-lere ayirmaq
"""def sirala():
    folder=input("Siralanacaq folder: ")
    files=[] #file-lar yigilacaq
    uzantilar=[] # uzantilar yigilacaq
    def list_dir():
        for file in os.listdir(folder):
            if os.path.isdir(os.path.join(folder,file)): # file folder-dir mi?
                continue
            if file.startswith("."):  # file hide-dirmi?
                continue
            else:
                files.append(file)
    list_dir()
    # Uzantilari almaq
    for file in files:
        uzanti=file.split(".")[-1]
        if uzanti in uzantilar:  # Uzanti daha evvel elave olundu?
            continue
        else:
            uzantilar.append(uzanti)
    for uzanti in uzantilar:  # folder yaradilir
        if os.path.isdir(os.path.join(folder,uzanti)):
            continue
        else:
            os.mkdir(os.path.join(folder,uzanti))
    for file in files:
        uzanti=file.split(".")[-1]
        os.rename(os.path.join(folder,file),os.path.join(folder,uzanti,file))
sirala()"""
# file-lari tarixlerine gore folder-lere ayirmaq
def tarixle():
    folder = input("Ayrilacaq folder: ")
    files = []  # file-lari yigacaq
    tarixler = []  # tarix-leri yigacaq
    def tarix_dir():
        for file in os.listdir(folder):
            if os.path.isdir(os.path.join(folder, file)):  # file folder-dir mi?
                continue
            if file.startswith("."):   # file hide-dir mi?
                continue
            else:
                files.append(file)
    tarix_dir()
    # Tarixleri almaq
    for file in files:
        tarix_damgasi = os.stat(os.path.join(folder, file)).st_birthtime
        tarix = datetime.fromtimestamp(tarix_damgasi).strftime("%d-%m-%Y")
        if tarix in tarixler:  # tarix daha evvel elave olunub?
            continue
        else:
            tarixler.append(tarix)
    for tarix in tarixler:
        if os.path.isdir(os.path.join(folder, tarix)):
            continue
        else:
            os.mkdir(os.path.join(folder, tarix))
    for file in files:
        tarix_damgasi = os.stat(os.path.join(folder, file)).st_birthtime
        tarix = datetime.fromtimestamp(tarix_damgasi).strftime("%d-%m-%Y")
        os.rename(os.path.join(folder, file), os.path.join(folder, tarix, file))
tarixle()

