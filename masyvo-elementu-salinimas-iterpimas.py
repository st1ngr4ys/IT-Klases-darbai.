#elemento salinimas 
from random import randint #pirmakart matau toki cikla?
sarasas = int(input("Kiek elemantu turi masyvas? sarasas="))
li = [randint(-50,50)for i in range(sarasas)]
print(li)
reiks = int(input("Kuri masyvo reiksme salinama? reiks="))
m = []
for i in range(sarasas):
    if reiks != a[i]:
        b.append(a[i])
print(m)

#Masyvo iterpimas i saraso pradzia 
li = [1,2,2,4,6,34,78]
reiks = 45
li.append('') 
for i in range(len(li)-1,0,-1): 
    li[i] = li[i-1]
li[0] = reiks
print("Atnaujintas sarasas", li)