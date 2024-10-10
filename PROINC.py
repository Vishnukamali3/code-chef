# cook your dish here
t=int(input())
for i in range(0,t):
    x,y=map(int,input().split())
    a=(10/100)*x
    print(int(a+y))