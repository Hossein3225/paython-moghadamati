x = input()
x = x.split("+")
for i in range(0,len(x)):
	x[i] = int(x[i])
x.sort()

khoroji = ""
for i in x:
    khoroji += ("+"+str(i))
khoroji  =khoroji.strip("+")
print(khoroji)
