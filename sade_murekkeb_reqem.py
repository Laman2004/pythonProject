#eded=int(input("Ededi daxil edin "))

# sade veya murekkeb olmasi
"""check=True
for i in range(2,eded):
    if eded % i==0:
        check=False                          
        break
if check==True:
    print(f"{eded}  sade ededdir")
else:
    print(f"{eded}  murekkeb ededdir")"""

# Musbet bolenlerin sayi
"""count=0
for i in range(1,eded+1):
    if eded%i==0:
        count+=1
print(f"{eded}-in musbet bolenlerinin sayi {count}-dir")"""

# ededin reqemleri cemini tapmaq
toplam=0
# 1-ci usul
"""str_s=str(eded)   # string-e cevirerek
for i in str_s:
    toplam+=int(i)
print(toplam)"""
# 2-ci usul
"""while eded!=0:
    c=eded%10         # riyazi yolla
    toplam+=c
    eded=eded//10
print(toplam)"""

# ekrandan daxil edilen 5 ededin en boyuk ve kiciyini tapin
"""liste=[]
for i in range(5):
    rakam=int(input("Eded daxil edin: "))
    liste.append(rakam)
print(f"En boyuk eded : {max(liste)}")
print(f"En kucuk eded : {min(liste)}")"""

# ekrandan daxil edilen ededin her hansi ededin kvadrati olub-olmadigini yoxlayan proqram

# 1-ci usul
"""eded=int(input("Eded daxil edin: "))
check=False
for i in range(1,eded):
    if eded/i==i:
        check=True
        break
if check==True:
    print(f"{eded}  {i}-in kvadratidir")
else: print(f"{eded} tam ededin kvadrati deyil")

# 2-ci usul
kvadrat=eded**0.5
if kvadrat==int(kvadrat):
    print("Kvadratidir")
else: print("Kvadrati deyil")"""

# ekrandan daxil edilen sozde hansi herifin nece defe islendiyini tapan proqram
"""metn=input("Ifade veya soz daxil edin: ")
sozluk=dict()
for harf in metn:
    if harf in sozluk:
        sozluk[harf]+=1
    else:
        sozluk[harf]=1
for harf,say in sozluk.items():
    print(harf,say)"""

# ekrandan daxil edilen metnde a harf-larini boyuk eden program
"""metn=input("Metn daxil edin: ")
metn1=""
for harf in metn:
    if harf=="a":
        metn1+="A"
    else:
        metn1+=harf
print(metn1)"""

# ilk 10.000 sade ededin necesi 3-le baslayib 7-le biter
"""list1= list()
list1.append(2)
say=3
while True:
    check=True
    for i in range(2,int(say**0.5)+1):      # proqramin suretini artirmaq ucun 
        if say%i==0:
            check=False
            break
    if check:
            list1.append(say)
    if len(list1)==10000:
        break
    say+=1
list2=[]
for j in list1:
    strcheck=str(j)
    if strcheck.startswith("3") and strcheck.endswith("7"):
        list2.append(j)
print(list2)"""

# 3 reqemli ededlerin necesi reqemlerinin kublari cemine beraberdir(Armstrong ededleri)
"""sum_list=[]
for reqem in range(100,1000):
    sum=0
    say=reqem
    while say!=0:
        c=say%10
        sum+=c**3
        say=say//10
    if sum==reqem:
        sum_list.append(reqem)
print(sum_list)"""

# Fibonacci ededlerinin 100-unu cap edin
"""fibo_list=[]
fibo_list.append(1)
fibo_list.append(1)
index=2
for i in range(2,100):                                     
    fibo_list.append(fibo_list[i - 2] + fibo_list[i - 1])   # for-la
while True:
    fibo_list.append(fibo_list[index-2]+fibo_list[index-1])   # while-la
    index+=1
    if len(fibo_list)==100:
        break
print(fibo_list)"""

# 100 reqemli ilk fibonacci ededini ve sira nomresini cap edin
"""fibo_list=list()
fibo_list.append(1)
fibo_list.append(1)
index=2
while True:
    fibo_list.append(fibo_list[index-2]+fibo_list[index-1])
    deyisken=fibo_list[index-2]+fibo_list[index-1]
    if len(str(deyisken))==100:
        print(deyisken)
        print(index)
        break
    index+=1"""













