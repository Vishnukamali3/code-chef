# cook your dish here
def song(n,x):
    if n>x:
        a=x*3
        b=n//a
        print(b)
    else:
        print("0")
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    song(n,x)