# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if a<=b and b>=c:
        print("YES")
    else:
        print("NO")