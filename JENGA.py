# cook your dish here
def jenga(n,x):
    if n<=x:
        print("yes")
    else:
        print("NO")
t=int(input())
while t>0:
    n,x=map(int,input().split())
    t-=1
    jenga(n,x)