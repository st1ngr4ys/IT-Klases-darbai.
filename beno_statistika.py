komanda = []
taskai = []
atkovoti_kamuoliai = []
blokai = []

with open("Duomenys.txt", "r") as f:
    n = int(f.readlne().strip())
    for _ in range(n):
        line = f.readline().strip().split()
        komanda.append(line[0])
        taskai.append(int(line[1]))
        atkovoti_kamuoliai.append(int(line[2]))
        blokai.append(int(line[3]))
