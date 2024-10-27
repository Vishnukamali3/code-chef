# cook your dish here
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if n>m:
        a=2*n
        print(a-m)
    else:
        print(n)