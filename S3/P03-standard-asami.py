
def standard(esm):
    esm = esm.capitalize()
    return (esm)

tedad = 10
l_esm = []

while tedad !=0:
    esm = input()
    esm_stan = standard(esm)
    l_esm.append(esm_stan)
    tedad -= 1
for esm in l_esm:
    print(esm)
