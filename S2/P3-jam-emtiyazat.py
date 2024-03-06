
emtiyaz_kol = 0
bord = 0
tedad = 30

while tedad!=0 :
    emtiyaz = int(input())
    emtiyaz_kol += emtiyaz
    if emtiyaz == 3:
        bord += 1
    tedad -= 1

print(emtiyaz_kol , bord)
