# cook your dish here
t=int(input())
while t>0:
    x,a,b=map(int,input().split())
    t-=1
    res=a+(b*2)
    if res>=x:
        print("Qualify")
    else:
        print("NotQualify")
    