# 2) Duomenų faile duomF4.txt surašyti parduotuvėje parduodamų akvariumų matmenys centimetrais.
# Parašykite programą, kuri nuskaitytų duomenis iš duomenų failo ir atspausdintų matmenis tų akvariumų, kurių tūris litrais didesnis už 50 l.
# (1l = 1 dm3, tad pirmiausiai verta matmenis pasiversti į dm, o tuomet jau skaičiuoti tūrį.)
# Programoje turi būti naudojama funkcija, kuri tikrintų, ar akvariumo tūris didesnis nei 50l. Ši funkcija turi gražinti atsakymą True/False.

with open("C:/Users/m.anejur/klases_darba/duomF4.txt") as f:
    duom = f.read()
    duom = map(int(), duom.split()) 
    print(duom)

# def ar_daugiau(x,y,z):
#     if x*y*z > 50:
#         return True 
#     return False

# print("Akvariumai, kurių tūris didesnis už 50 l: ")
# for i in range(len(duom)):
#     if i%3==0:
#         x = [i]
#         y = [i+1]
#         z = [i+2]
#         didesnis = ar_daugiau(x/10, y/10, z/10)
#         if didesnis:
#             print(x,y,z)