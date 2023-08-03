liste=[1,2,3,4,5,6,9]
"""list1=[]
for i in list:
    list1.append(i)
print(list1)
list2=[i for i in liste]
print(list2)"""

"""list1=[]
for i in list:
    list1.append(i*i)
print(list1)
list2=[i*i for i in liste]
print(list2)"""

"""list1=[]
for i in liste:
    if i%2 ==0:
        list1.append(i)
print(list1)
list2=[i for i in liste if i%2 ==0]
print(list2)"""

"""list1=[]
for i in list:
    if i%2 ==0:
        continue
    list1.append(i)
print(list1)
list2=[i for i in list if not i%2 ==0]
print(list2)"""

"""list1=[]
letter="abc"
for i in liste:
    for j in letter:
        list1.append((i,j))
print(list1)
list2=[(i,j) for i in liste for j in letter]
print(list2)"""

"""list_=[(1,2,3),(4,5,6),(7,8,9)]
list1=[]
for i in list_:
    for j in i:
        list1.append(j)
print(list1)
list2=[j for i in list_ for j in i]
print(list2)"""

print(dir(list))
list_method=[]
for method in dir(list):
    if method.startswith("__"):
        continue
    list_method.append(method)
print(list_method)
list_method1=[method for method in dir(list) if not method.startswith("__")]
print(list_method1)
