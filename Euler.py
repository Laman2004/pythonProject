import math
import functools
""" 1-ci sual
def check(x):
    if x%3==0 or x%5==0:
        return True
    else:
        return False

sum=0
for i in range(1,1000):
    if check(i):
        sum+=i
print(sum)"""

# 2-ci sual
"""fibo_list=list()
fibo_list.append(1)
fibo_list.append(2)
index=2
while True:
    if fibo_list[index-2]+fibo_list[index-1]<4000000:
        fibo_list.append(fibo_list[index-2]+fibo_list[index-1])
        index+=1
    else:
        break
sum=0
for i in fibo_list:
    if i%2==0:
        sum+=i
print(sum)
print(index)"""

# 3-cu sual
"""def funksiya(x):
    check=True
    for j in range(2,int(math.sqrt(x))+1):
        if x%j==0:
            check=False
            continue
    return check

num=600851475143
biggist=1
for i in range(2,int(math.sqrt(num))):
    if num%i==0 and funksiya(i):
        biggist=i
print(biggist)"""

# 4-cu sual
"""def polindrom(x):
    if str(x)==str(x)[::-1]:
        return True
    else:
        return False
big_poli=0
for i in range(100,1000):
    for j in range(100,1000):
        if polindrom(i*j) and i*j>big_poli:
            big_poli=i*j
print(big_poli)"""

# 5-ci sual
"""def gcd(x,y):
    return math.gcd(x,y)    #EBOB
def lcm(x,y):
    return (x*y)//gcd(x,y)    # EKOB
liste=range(1,21)
netice=functools.reduce(lcm,liste)
print(netice)"""

# 6-ci sual
"""def kvadrat():
    sum=0
    for i in range(1,101):
        sum+=i*i
    return sum
def cem_kvadrat():
    cem=0
    for i in range(1,101):
        cem+=i
    return pow(cem,2)
print(cem_kvadrat()-kvadrat())"""

# 7-ci sual
"""say=0
def prime_check(x):
    check=True
    if x==2:
        return True
    else:
        for i in range(2,int(math.sqrt(x)+1)):
            if x%i==0:
                check=False
                break
        return check

i=2

while True:
    if prime_check(i):
        say+=1
    if say==10001:
        print(i)
        break
    i+=1"""

# 8-ci sual
sayi = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""
liste = sayi.split("\n")
print(liste)
number = ""
for i in liste:
    number += i
product = 0
for i in range(0, len(liste)-12):
    aux = 1
    for j in number[i:i+13]:
        aux *= int(j)
    if aux > product:
        product = aux
print(product)





