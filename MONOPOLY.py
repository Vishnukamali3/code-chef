# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=list(map(int,input().split()))
    a=max(x,y,z)
    b=(x+y+z)-a
    if b<a:
        print("YES")
    else:
        print("NO")
    
    