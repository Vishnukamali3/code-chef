# cook your dish here
t=int(input())
while t>0:
    x,y=map(int,input().split())
    t -=1
    a=x*100
    b=y*10
    if a<b:
        print("Disposable")
    else:
        print("Cloth")