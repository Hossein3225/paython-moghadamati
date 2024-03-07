x = input().lower()
l = []

for i in x:
    l.append(i)

l.reverse()
khoroji = ""
for i in l:
    khoroji += i

if khoroji == x :
    print("palindrome")
else:
    print("not palindrome")