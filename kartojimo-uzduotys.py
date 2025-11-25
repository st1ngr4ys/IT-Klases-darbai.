#1 Parasyti funkcija kuri suskaiciuos sk suma nuo 1 iki n 
#funcijos pavadinimas - sum_to_n(n)
# n = int(input("Koks n?: "))
# def sum_to_n(n):
#     suma = 0
#     for i in range(n):
#        suma += i
#     print(suma)
# sum_to_n(n) #bijau cia neteisinga bet nu ka as zinau 

#2 kiek kartu pasirodo duotas simbolis?
# string = input("Iveskite string: ")
# ieskomas_char = input("Ieskomas simbolis: ")
# def count_char(string, ieskomas_char):
#     char=0
#     for simboliai in string:
#         if simboliai in ieskomas_char:
#             char += 1
#     return char

# print("kiek kartu pasirodo duotas simbolis: ",count_char(string, ieskomas_char))


# 3 Funkcija, kuri sukeicia 2 masyvo elementu vietas
# list = [1, 2, 3]
# n = len(list)
# def swap(list):
#     for i in range(0, n-1, 2):
#         list[i], list[i+2] = list[i+2], list[i] #nesuprantu kodel man priestai neleido to (i+2) daryti bet bent jau dabar veikia
#     return list 

# print(swap(list))

#4 Funkcija, kuri iterpia elementa i duota pozicija (nenaudojant insert)
from random import randint
n=int(input("kiek elementu sarase?: "))
list = [randint(10, 50)for i in range(n)]
elementas = input ("elementa, kuri norite iterpti: ")
index = 3
print(list)
def insert_at(list, index, elementas):
    list.append("") 
    for i in range(n, index-1, -1):
        list[i]= list[i-1]
    list[index] = elementas
    return list
print("Naujasis sarasas - ", insert_at(list, index, elementas))