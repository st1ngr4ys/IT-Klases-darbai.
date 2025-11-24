#5. Funkcija: remove_at(arr, index) Nenaudoti pop(). 
# from random import randint 
# n = int(input("Kiek elementu turi masyvas?: "))
# list = [randint(1,50)for i in range(n)]
# print(list)
# index = int(input("Kurio masyvo reiksme salinama? "))
# def remove_at(list, index):
#     naujas_list = [] #masyvas kuriame surasomos visos masyvo list reiksmes?? pagavau kampa cia yra daromas kitas sarasas be nurodyto index
#     for i in range(n):
#         if index != list[i]:
#             naujas_list.append(list[i])
#     return naujas_list
# print("masyvas be nurodyto elemento - ", remove_at(list, index)) # is pirmo karto pavyko yaaaayyyyy!!!!


#6 Parašyk funkciją, kuri apsuka masyvą (reverse), nenaudojant reverse(). Pvz.: reverse([1,2,3]) → [3,2,1]
# from random import randint 
# n = int(input("Kiek elementu turi masyvas?: "))
# list = [randint(1,50)for i in range(n)]
# print(list)
# def reverse(list):
#     for i in range(n//2): #kodel sarasas dalinamas per puse?
#         list[i], list[n-1-i] = list[n-1-i], list[i]
#     return list
# print("saraso reversas - ", reverse(list)) #yaaayy irgi pavyko is pirmo karto!! be vadovelio negaleciau...

#2var 
from random import randint 
n = int(input("Kiek elementu turi masyvas?: "))
list = [randint(1,50)for i in range(n)]
print(list)
def reverse(list):
    list = list[:: -1]
    return list
print(reverse(list))


#7 Parašyk funkciją, kuri sukuria naują masyvą, kuriame likę tik lyginiai skaičiai. Pvz.: filter_even([1,2,3,4]) → [2,4] 

# from random import randint 
# n = int(input("Kiek elementu turi masyvas?: "))
# list = [randint(-20,60)for i in range(n)]
# print(list)
# even_num = []
# def filter_even(list):
#     for i in range(n):
#         if list[i]/2 == 0: #cia rasoma klaida bet neissiaiskinu kodel? "list index out of range"????
#             even_num.append(list[i])
#     return even_num
# print("Naujas masyvas - ", filter_even(even_num))


#8 Įgyvendink bubble sort algoritmą. Funkcija: bubble_sort(arr) Naudoti while arba for, elementus sukeisti rankiniu būdu, rikiuoti didėjimo tvarka.
# from random import randint 
# n = int(input("Kiek elementu turi masyvas?: "))
# list = [randint(-20,60)for i in range(n)]
# print(list) 
# def bubble_sort(list):
#     for i in range(n-1):
#      for j in range(n-2,i-1, -1):
#          if list[j+1] < list[j]:
#              list[j], list[j+1] = list[j+1], list[j]
#     return list
# print("surikiuotas masyvas - ", bubble_sort(list)) 


#9 Parašyk funkciją, kuri bubble sort principu surikiuoja kiekvieną 2 ilgio masyvo segmentą (porą). Pvz.: iš [5, 1, 4, 2] gaunama [1,5, 2,4].
# from random import randint 
# n = int(input("Kiek elementu turi masyvas?: "))
# list = [randint(1,99)for i in range(n)]
# print(list) 
# def pair_sort(list):
#     for i in range(n-1):
#      for j in range(n-2,i-1, -2):
#          if list[j+1] < list[j]:
#              list[j], list[j+1] = list[j+1], list[j]
#     return list 
# print (pair_sort(list)) # Veikia, bet tik kai n yra lyginis sk


#10 Parašyk funkciją, kuri:
# a) pašalina visus neigiamus skaičius iš masyvo,
# b) surikiuoja likusius skaičius bubble sort metodu,
# c) grąžina surikiuotą masyvą.

# from random import randint 
# n = int(input("Kiek elementu turi masyvas?: "))
# list = [randint(-86,26)for i in range(n)]
# print(list) 
# m = []
# def remove_negativ(list):
#     for i in range(n):
#         if list[i]>0:#??????????????????????????????
#             m.append(list[i])
#     return m
# print(remove_negativ(m))#?????????????