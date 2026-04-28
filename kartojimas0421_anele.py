with open("C:/Users/m.anejur/Documents/Anele/duom3.txt") as f:
    n=f.readline()
    eilutes = []
    for _ in range(int(n)):
        m = f.readline()
        m = m.split()
        for i in range(len(m)):
            m[i] = int(m[i])
        eilutes.append(m)

print(eilutes)


def sum_neig(m):
    sum=0
    for i in m:
        if i<0:
            sum+=i
    return sum


def nelyg_sk(m):
    nelyg = 0
    for s in m:
        if s%2!=0:
            nelyg+=1
    return nelyg


for eilute in eilutes:
    print(eilute)
    print("neig sk suma", sum_neig(eilute))
    print("nelyginiu: ",nelyg_sk(eilute))