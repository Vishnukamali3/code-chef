# cook your dish here
def alice():
    t=int(input())
    for i in range(0,t):
        a,b=map(int,input().split())
        c=(a+b)
        if c%2==0:
            print("YES")
        else:
            print("NO")
alice()
            