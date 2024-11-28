# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    for i in range(y):
        if x<=1000:
            x=x+1000
        else:
            x=x*2
    print(x)
        