tedad = int(input())

dict = {}
while tedad != 0 :
    kalame = input()
    kalame = kalame.split()
    dict[kalame[0]] = kalame[1]

    tedad -= 1

jomle = input()

l_jomle = jomle.split()

while len(l_jomle) != 0:
    kalame = l_jomle.pop(0)
    jomle = jomle.replace(kalame ,dict.get(kalame,kalame))

print (jomle)