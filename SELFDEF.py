# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    c=0
    a=list(map(int,input().split()))
    for i in range(len(a)):
        if a[i]>=10 and a[i]<=60:
            c=c+1
    print(c)