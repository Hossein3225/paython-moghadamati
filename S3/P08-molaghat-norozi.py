x = input()
x = x.split()
l_x = []
for i in x:
    l_x.append(int(i))

l_x.sort()

jabejaii1 = l_x[1] - l_x[0]
jabejaii2 = l_x[2] - l_x[1]
jam_jabejaii = jabejaii1 + jabejaii2
print(jam_jabejaii)