
# 1) Parašykite programą, kuri apskaičiuotų ritinio paviršiaus plotą ir tūrį (atsakymus suapvalinkite 0,1 tikslumu). Ritinio pagrindo spindulio ilgis ir aukštis įrašyti į duomenų failą duomF3.txt.

# Programoje turi būti naudojamos trys funkcijos:
# · duomenų nuskaitymo funkcija;
# · ritinio paviršiaus ploto skaičiavimo funkcija; Spav.=2πr(r+h)
# · ritinio tūrio skaičiavimo funkcija. V=πr2h
 

from math import pi 
with open("C:/Users/m.anejur/klases_darba/DuomF3.txt") as f:
    spindulys= int(f.read(1))
    aukstis= int(f.read(2))
    
    print("spindulys", spindulys, "aukstis: ", aukstis)

def pavirs_plotas(spindulys, aukstis):
    S = 2*pi*spindulys*(spindulys + aukstis)
    return S 
print("Paviršiaus plotas =",round(pavirs_plotas(spindulys, aukstis),1)) 

def tūris(spindulys, aukstis):
    V= pi*(spindulys**2)*aukstis
    return V
print("tūris = ",round(tūris(spindulys, aukstis),1))
