# cook your dish here
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    e=n//2
    o=n-e
    if x%2==0:
        print(e)
    else:
        print(o)            