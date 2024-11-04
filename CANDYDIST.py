# cook your dish here
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=n//m
    if n%m!=0 or a%2!=0:
        print("NO")
    elif a%2==0:
        print("YES")