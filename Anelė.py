## Kontrolinis darbas iš Python programavimo
## Praktinė dalis 25-40 min

# ----------------------------------------
#
#  STRUKTŪRA:
#  1. Kodo supratimo klausimai
#  2. Mažos programavimo užduotys
#  3. Didžioji programavimo užduotis
#
#  Atsakymus rašykite tiesiog šiame faile.
#
#  Priminimas: pažymėjus kelias eilutes, jas užkoduoti galima su ctrl + ?
# ----------------------------------------

# ========================================
# 1 DALIS – KODO SUPRATIMO KLAUSIMAI
# ========================================

# # KLAUSIMAS 1. Kodėl antram kintamajam naudojama int() funkcija?
# vardas = input("Koks tavo vardas? ")
# skaičius = int(input("Įvesk skaičių nuo 1 iki 100: "))

# print("Labas", vardas, "tavo skaičius", skaičius * 5)

# ATSAKYMAS: Int funkcija paverčia naudotojo įvestą tekstą į skaičių. 
# teisingai, 2/2 balo.

# # KLAUSIMAS 2. Kam iš esmės reikalinga eilutė i = i + 1 ?
# i = 0
# while i < 5: 
#     print(i)
#     i = i + 1 

# # ATSAKYMAS: Kitaip bus begalinis ciklas, nes i visuomet būtų lygus 0
# tesingai, 2/2 balo.

# # KLAUSIMAS 3. Ką darys žemiau esančio kodo dalis?

# password = ''
# while password != "Coding_is_fun!":
#     password = input()

# # ATSAKYMAS: while cikle tikrina ar kintamasis password yra nelygus "Coding_is_fun!",
#  jei taip nelygu tai leidžia naudotojui įvesti nauja reikšmą kintamajame. 
# teiginai, 1/1 balo.

# # KLAUSIMAS 4. 
# # Perskaityk šį kodą ir parašyk:
# # - ką programa atspausdins,
# # - paaiškink savo žodžiais, kodėl taip gaunasi.

# x = 4
# numbers = [10, 20, 30, 40, 50]
# result = numbers[x % 3] 

# # Ką atspausdins programa? nieko, nes nėra print funkcijos. #good catch :) 1/1
# # Paaiškinimas, kodėl taip gaunasi (2–3 sakiniai): 
# Yra kintamasis x kurio reiksme 4, masyvas numbers ir result kurio reiksmė nurodo iš sarašo numbers pozicija paėmus x modulį iš 3. 
# result kintamasis nurodo 1 numbers sarašo pozicija kas yra 20 

#Šaunuolė, puikiai 1/1 balo. 


# ========================================
# 2 DALIS – MAŽOS PROGRAMAVIMO UŽDUOTYS
# ========================================

# UŽDUOTIS 1.
# Užpildyk trūkstamą kodo dalį: funkcija turi suskaičiuoti, kiek kartų sąraše pasirodo elementas target.
# lst = [1, 2, 3, 4, 5, 6, 1]
# target = 1
# def count_occurrences(lst, target):
#     count = 0
#     for item in lst:
#         if item == target: # čia reikia pakeisti vieną dalyką. Darsyk perskaityk užduotį ir pagalvok, ką su kuo tikrini. Ko ieškai?
#             count += 1 #nevisai, yra maža klaidelė
#             # arba count = count + 1
#         # TODO_: Pridėti trūkstamas eilutes
#     return count
# print(count_occurrences)

# 2/3 balo. 

# UŽDUOTIS 2.
# Parašyk vieną eilutę, kuri pridėtų skaičių 99 į sąrašo pabaigą.
# numbers = [1, 2, 3, 4]
# # TODO_: Viena eilutė:
# numbers.append(99)
# print(numbers)

# # 0/1 balo. Neatlikta. #galimai kazkaip praleidau?? 

# # UŽDUOTIS 3.
# # Pakeisk kodą taip, kad atspausdintų TAU tinkantį sakinį (turi išsirinkti 1 arba 2 sakinio pabaigos žodžius po dvitašakio).
# # Negali keisti kintamojo "tekstas"

# tekstas = "Man programuoti su Python sekasi: labai gerai blogai neblogai"
# print(tekstas[0:33] + tekstas[52:61])

# 2/2 balai. Nors manau, kad tau sekasi gerai :)

# ========================================
# 3 DALIS – DIDŽIOJI UŽDUOTIS
# ========================================

"""
Sukurk programą.
Jei kažkurio žingsnio padaryti negali, pakeisk jį paprastesniu, kad galėtum dirbti toliau.

Programa turi:
1. Paprašyti vartotojo įvesti N skaičių (kiek skaičių įves).
2. Sukurti tuščią sąrašą.
3. For ciklu surinkti visus įvestus skaičius į sąrašą. 
4. Suskaičiuoti, kiek sąraše yra lyginių skaičių.
5. Surikiuoti sąrašo elementus didėjimo tvarka su bubble sort.
6. Paslinkti visus saraso elementus į kairę (kokiu nori būdu).
7. Aiškiai atspausdinti rezultatus.

"""

# TODO_: Tavo sprendimas:

# lst = from n import randint      # atsiprasau bet praktikos visai nemoku 
# # [1, 2, 4, 5, 3, 7, 5, 4, 9, 6]
# n = int(input("iveskite kiek elementu turi sarasas: ")) # 1 balas
# print(lst) 
# empty_lst = [] # 1 balas
# for i in lst:
#     for j in empty_lst:
#         empty_lst[j] = empty_lst[j] + lst[i]
# print(empty_lst)

# 2/7 balo

# taisymas 
n = int(input("iveskite kiek elementu turi sarasas: ")) 
from random import randint
lst = [randint(10,65)for i in range(n)]
print(lst)
empty_lst= []
for i in lst:
    empty_lst.append(i)

print(empty_lst)

count = 0 
def kiek_lyg(lst):
    for i in lst:
        if i % 2 == 0:
            count +=1
    return count
print(kiek_lyg) 