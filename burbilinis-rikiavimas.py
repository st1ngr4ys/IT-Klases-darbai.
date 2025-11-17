# #burbilinis rikiavimas 
# from random import*
# n=int(input("Kiek elementu turi masyvas a? n= "))
# a = [randint(0,5) for i in range(n)]
# print("pradinis masyvas",a)
# for i in range(n-1):
#     for j in range(n-2,i-1, -1):
#         if a[j+1] < a[j]:
#             a[j], a[j+1] = a[j+1], a[j]
# print("Surikiuotas masyvas", a)

#Savarankiska uzduotis 
# from random import*
# n=int(input("Kiek yra krepsininku? n= "))
# a = [randint(160,200) for i in range(n)]
# print("krepsininku sarasas", a)
# for i in range(n-1, -1, -1): 
#     for j in range(0, i):  #akmens metodas
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print("Surikiuotas sarasas", a)
# print("Skirtumas tarp auksciausio ir zemiausio krepsininko", a[n-1] - a[0])

#2 sav. uzduotis 

from random import*
n=int(input("Kiek elementu? n= "))
a = [randint(-10,30) for i in range(n)]
print("pradinis masyvas", a)
rik_pozym = 1 
for i in range(n-1, -1, -1):
    if rik_pozym == 0:
        break
    rik_pozym = 0
    for j in range(0,i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            rik_pozym += 1
print("surikiuotas masyvas", a)