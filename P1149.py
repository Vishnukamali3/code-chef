# cook your dish here
x,y,k=map(int,input().split())
z=abs(x-y)
if z<=k:
    print("YES")
else:
    print("NO")