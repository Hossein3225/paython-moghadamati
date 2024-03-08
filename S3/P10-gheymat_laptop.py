tedad = int(input())

tedad_avaliye = tedad
z = 0
c = 0

while tedad != 0:
    x = input().split()
    gheymat , keyfiyat = x
    gheymat , keyfiyat = int(gheymat) , int(keyfiyat)

    #برای اینکه مبنای اولیه دستمون بیاد
    if tedad == tedad_avaliye:
        gheymat_ = gheymat + 1
        keyfiyat_ = 0

    if gheymat < gheymat_ and keyfiyat > keyfiyat_:
        gheymat_  , keyfiyat_ =  gheymat , keyfiyat
        c += 1    
    elif gheymat > gheymat_ and keyfiyat <keyfiyat_ :
        z += 1

    tedad -= 1


if c > 1 :
    print("happy irsa")
elif z > 1 :
    print("happy irsa")
else:
    print("poor irsa")