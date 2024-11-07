# cook your dish here
t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    x=n//2
    if n%2==0:
        y=x*a+x*b
        print(y)
    elif n%2!=0:
        print((x*a)+(x+1)*b)