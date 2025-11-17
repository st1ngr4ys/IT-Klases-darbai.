# def teisingas_slap(passw):
#     sk=False
#     for raide in passw:
#         if raide.isdigit():
#             sk=True
#         else:
#             sk=sk or False
#     if len(passw)>7 and sk:
#         return True
#     else: 
#         return False

# slaptazodis=input("Įvesk slaptažodį: ")
# ar_teisingas = teisingas_slap(slaptazodis)
# #MK pabaik kodą: jeigu teisingas, atspausdink "geras slaptazodis"
# #priešingu atveju - "Slaptažodis neatitinka reikalavimų" arba panašiai :)
# print("geras slaptazodis")

# def patikrink_slap(slap):
#     while slap != "Coding_is_fun":
#         slap=input("iveskite teisinga splatazodi: ")
#         if slap != "Coding_is_fun":
#             print("Neteisinga bandykite dar karta")
#         else:
#             print("Teisinga!") 

# slap=input() #trūksta, kad terminale matytųsi, ko nori iš vartotojo :)
# patikrink_slap(slap)

# def tiesines_paeiska(sarasas, ieskomas_el):
    
#     for i in range(len(sarasas)):
#         if sarasas[i] == ieskomas_el :
#             return i
#     return -1

# sarasas=[1,34,56,456,78]
# ieskomas_el=56

# print(tiesines_paeiska(sarasas,ieskomas_el)) 


# # TIESINES paieškos FUNKCIJOS 1 UZDUOTIS
# #MK funkcijos yra įvairios ir skirtingos.
# # Šitpje užduotyje tu kuri funkciją, kuri atlieka tiesinę paiešką.
# sarasas=["palapine","maistas","zemelapis","miegmaisis","rubai","batai"]

# def ties_funkcija(sarasas, ieskomas_daiktas):
#     for i in range(len(sarasas)):
#         if sarasas[i] == ieskomas_daiktas:
#             return i
#     return -1

# ieskomas_daiktas = "rubai"
# print("Ieškomas daiktas:",ieskomas_daiktas)
# if ties_funkcija(sarasas,ieskomas_daiktas) > 0:
#     print("Daiktas rastas")
# else: 
#     print("Nerasta")

# #TIESINES paieškos FUNKCIJOS 2 UZDUOTIS 
# #MK neužbaigta. Pradžia daug žadanti
# daiktas1=[""]
# daiktas2="daiktas"

# def string_daiktai(daiktas2, daiktas1):
#     if daiktas2 == daiktas1 :
#         return "yra"

# def kiek_daiktu()