# cook your dish here
t=int(input())
for i in range(t):
    n,k,m=map(int,input().split())
    bag=k*m
    if n%bag==0:
        print(n//bag)
    else:
        print((n//bag)+1)