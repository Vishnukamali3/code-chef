# cook your dish here
t=int(input())
while t>0:
    x,y,z=map(int,input().split())
    t-=1
    a=10*x
    if y<=a:
        print(y*z)
    else:
        print(a*z)