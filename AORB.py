# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=x*2
    b=(x+y)*4
    c=y*4
    d=(x+y)*2
    e=500-a+1000-b
    f=1000-c+500-d
    print(max(e,f))
    