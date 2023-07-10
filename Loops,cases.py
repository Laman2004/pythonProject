sayi =[1,2,3,5,7,8,0]
i=10
"""for i in sayi:      # for-un istifadesi
    print(i)
a=["a","b","c"]
b=[1,3,5]
for i in a:        # nested for
    for j in b:
        print(i,j)
eded=5
eded1=7
eded2=5
if eded==eded2:                        # if ve else use
    print(f"{eded} = {eded2}")
else:
    print(f"{eded} != {eded2}")
num=3
num1=5
num2=8
if num1==num and num1!=num2:
    print("and")
elif num1==num or num1!=num2:          # elif,or,and use
    print("or")
else:
    print("hec biri")
ad="Feride"
ad1="Ferid"
ad1+="e"
if ad1==ad:
    print("Beraberdir")
if ad is ad1:                          # is ve == ferqi
    print("id-leri eynidir")
if not i in sayi:                          # if in ve not-la
    print("var")

while i<12:                           # while use
    print("12-den kicikdir")
    i+=1
for j in sayi:
    if j==3:
        continue
    print(j)  
for p in sayi:
    if p==3:
        break
    print(p) """
no=1
liste=range(1,10)                   # factorial
for j in liste:
    no*=j
    print(no)





