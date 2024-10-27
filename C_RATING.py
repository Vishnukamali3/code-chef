t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=y-x
    if a%8==0:
        print(a//8)
    elif y-x==0:
        print("0")
    else:
        print((a//8)+1)