# cook your dish here
t=int(input())
for i in range(t):
    c=0
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n):
        if l[i]%2==0:
            c=c+(l[i]//2)
        else:
            c=c+((l[i]//2)+1)
    print(c)