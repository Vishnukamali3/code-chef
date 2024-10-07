# cook your dish here
t=int(input())
for i in range(0,t):
    x,y=map(int,input().split())
    a=x*5
    if a>=y:
        print('YES')
    else:
        print("NO")