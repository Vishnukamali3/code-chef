# cook your dish here
t=int(input())
for i in range(1,t+1):
    n,x=map(int,input().split())
    if n%6==0:
        print((n//6)*x)
    else:
        print((n//6+1)*x)