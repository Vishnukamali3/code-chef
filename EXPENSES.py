# cook your dish here
t=int(input())
for i in range(t):
    n,x=list(map(int,input().split()))
    total=2**x
    for i in range(n):
        total=total-(total//2)
    print(total)
        