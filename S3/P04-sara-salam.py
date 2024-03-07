x = input()

h = x.find("h")
e = x.find("e",h)
l = x.find("l",e)
L = x.find("l",l+1)
o = x.find("o",L)

if h<e<l<L<o :
    print("YES")
else:
    print("NO")
