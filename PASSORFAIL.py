# cook your dish here
t=int(input())
for i in range(t):
    n,x,p=map(int,input().split())
    inc=n-x
    to=x*3
    a=to-inc
    if a>=p:
        print("PASS")
    else:
        print("FAIL")