from math import sqrt

tedad = int(input())

l_sq = []
while tedad != 0 :
    adad = int(input())
    adad_sq = sqrt(adad)
    adad_sq = "%.9f"%adad_sq
    l_sq.append(adad_sq[:-5])
    tedad -= 1

for i in l_sq:
    print(i)
