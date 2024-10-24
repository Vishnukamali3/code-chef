# cook your dish here
t=int(input())
while t>0:
    a,b=map(int,input().split())
    t-=1
    x=(a*100)//10
    y=(b*100)//20
    if x==y:
        print("ANY")
    elif x>y:
        print("FIRST")
    else:
        print("SECOND")