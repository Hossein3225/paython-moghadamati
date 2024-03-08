tedad_bazikon = int(input())
salhay_bazi = input()

salhay_bazi = salhay_bazi.split()

c = 0
for salbazi in salhay_bazi:
    if int(salbazi) <= 2 :
        c += 1

tedad_tim = c//3
print(tedad_tim)