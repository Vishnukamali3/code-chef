# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    x=(a*100)//100
    y=(b*200)//100
    m=100-x
    n=200-y
    if m<n:
        print("FIRST")
    elif m>n:
        print("SECOND")
    else:
        print("BOTH")
    