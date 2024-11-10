# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=(10/100)*x
    b=x-a
    if b<y:
        print("ONLINE")
    elif b==y:
        print("EITHER")
    else:
        print("DINING")