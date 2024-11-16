# cook your dish here
t=int(input())
for i in range(t):
    a,b,x,y=map(int,input().split())
    m=a/x
    n=b/y
    if m<n:
        print("CHEF")
    elif m>n:
        print("Chefina")
    elif m==n:
        print("BOTH")