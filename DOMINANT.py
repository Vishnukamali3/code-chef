# cook your dish here
def army(x,y,z):
    a=max(x,y,z)
    b=(x+y+z)-a
    if b<a:
        print("YES")
    else:
        print("NO")
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    army(x,y,z)
