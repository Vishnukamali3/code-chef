# cook your dish here
t=int(input())
for i in range(t):
    p,l=map(int,input().split())
    a=(l/p)*100
    if a>=75:
        print("YES")
    else:
        print("NO")