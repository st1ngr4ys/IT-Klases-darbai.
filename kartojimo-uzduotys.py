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
string = input("Iveskite string: ")
ieskomas_char = input("Ieskomas simbolis: ")
char=0
for simboliai in string:
    if simboliai in ieskomas_char:
        char += 1
print("kiek kartu pasirodo duotas simbolis: ", char)