x = input()
x = x.lower()
x=x.replace("a","")
x=x.replace("i","")
x=x.replace("u","")
x=x.replace("e","")
x=x.replace("o","")


c=""
for i in x:
    c+=("."+i)

print(c)

