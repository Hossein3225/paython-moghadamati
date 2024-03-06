

def maghsom_(x):
    c = 0
    for i in range(1,x+1):
        if x%i ==0:
            c += 1
    return(c)

tedad = 20
B_maghsom = 0
B_adad = 0

while tedad != 0:
    adad = int(input())
    maghsom = maghsom_(adad)
    if maghsom > B_maghsom :
        B_maghsom = maghsom
        B_adad = adad
    elif maghsom == B_maghsom and adad>B_adad:
        B_adad = adad

    tedad -=1


print(B_adad , B_maghsom)
