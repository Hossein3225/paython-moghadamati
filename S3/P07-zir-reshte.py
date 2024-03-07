x = input()
AB = x.find("AB")
BA = x.find("BA",AB+2)
if AB != -1 and  BA != -1:
        print("YES")
else:
    BA = x.find("BA")
    AB = x.find("AB",BA+2)
    if AB !=-1 and  BA != -1:
        print("YES")
    else:
        print("NO")
