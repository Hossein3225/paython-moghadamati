x = input()

l_a=[]
for i in range(ord("a"),ord("z")+1):
    l_a.append(chr(i))

l_A=[]
for i in range(ord("A"),ord("Z")+1):
    l_A.append(chr(i))

c_a = 0
c_A = 0
for i in x:
    if i in l_a:
        c_a += 1
    else:
        c_A += 1

if c_a >= c_A :
    print(x.lower())
else:
    print(x.upper())

