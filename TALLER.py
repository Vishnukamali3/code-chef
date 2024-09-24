# cook your dish here
def alice():
    t=int(input())
    for i in range(0,t):
        a,b=map(int,input().split())
        if a>b:
            print("A")
        elif b>a:
            print("B")
alice()

