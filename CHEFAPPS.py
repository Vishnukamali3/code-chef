# cook your dish here
t=int(input())
for i in range(t):
    s,x,y,z=map(int,input().split())
    a=s-(x+y)
    if a>=z:
        print("0")
    else:
        b=z-a
        if b<=max(x,y):
            print("1")
        else:
            print("2")