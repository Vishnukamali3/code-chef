# cook your dish here
t=int(input())
for i in range(t):
    x1,y1,x2,y2=map(int,input().split())
    a=abs(x1-x2)
    b=abs(y1-y2)
    print(max(a,b))