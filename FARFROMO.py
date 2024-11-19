# cook your dish here
t=int(input())
for i in range(t):
    x1,y1,x2,y2=map(int,input().split())
    a=((x1**2)+(y1**2))
    b=((x2**2)+(y2**2))
    if a>b:
        print("ALEX")
    elif b>a:
        print("BOB")
    else:
        print("EQUAL")