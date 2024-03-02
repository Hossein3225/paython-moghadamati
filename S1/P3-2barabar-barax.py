x = int(input())

x1 = x%10
x2 = int(x/10)%10
x3 = int(x/100)%10

x_n = x1*100+x2*10+x3
print(x_n)
