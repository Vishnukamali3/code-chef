# cook your dish here
def maximum():
    t=int(input())
    for i in range(0,t):
        a,b,c=map(int,input().split())
        x=max(a,b,c)
        y=min(a,b,c)
        print(x-y)
maximum()