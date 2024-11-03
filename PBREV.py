# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    c=0
    s=list(map(int,input().split()))
    for i in s:
        if i<=4:
            c=c+1
    if c==0:
        print("YES")
    else:
        print("NO")
        
        