# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    a=x*y
    b=x+z
    print(min(a,b))