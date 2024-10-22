# cook your dish here
t=int(input())
while t>0:
    a,b,c=map(int,input().split())
    t-=1
    if (a+b)%2==1 or (a+c)%2==1 or (b+c)%2==1:
        print("yes")
    else:
        print("NO")