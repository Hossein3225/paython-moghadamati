tedad = int(input())

l_ara = []
dict = {}

while tedad != 0:
    ray = input()
    l_ara.append(ray)
    dict[ray] = 1

    tedad -= 1

l_afrad = list(dict.keys())
l_afrad.sort()

while len(l_afrad) != 0:
    esm = l_afrad.pop(0)
    print(esm , l_ara.count(esm))

