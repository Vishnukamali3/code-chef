# cook your dish here
t=int(input())
for i in range(t):
    n,x,k=map(int,input().split())
    a=k//x
    print(min(n,a))