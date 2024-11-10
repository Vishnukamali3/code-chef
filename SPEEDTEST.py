# cook your dish here
t=int(input())
for i in range(t):
    a,x,b,y=map(int,input().split())
    m=a/x
    n=b/y
    if m>n:
        print("ALICE")
    elif m<n:
        print("BOB")
    else:
        print("EQUAL")