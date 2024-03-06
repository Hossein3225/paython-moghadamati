from random import randint

pasokh = ""
sar = 1
tah = 99

while pasokh!= "d":
    x = randint(sar,tah)
    print(x)
    pasokh = input()
    if pasokh == "k":
        tah = x-1
    elif pasokh == "b":
        sar = x+1
