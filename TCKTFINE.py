# cook your dish here
t=int(input())
for i in range(0,t):
    x,y,z=map(int,input().split())
    a=y-z
    b=a*x
    print(b)