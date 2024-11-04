# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if x<=3:
        print(x*y)
    elif x%3==0:
        a=(x//3)-1
        print(x*y+a*z)
    elif x%3!=0:
        b=(x//3)
        print(x*y+b*z)