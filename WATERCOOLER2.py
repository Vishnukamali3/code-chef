# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>=y:
        print("0")
    else:
        months=y//x
        if y%x==0:
            months=months-1
        print(months)