# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    a=z-y
    print(a//x)