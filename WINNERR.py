# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    x=max(a,b)
    y=max(c,d)
    if x<y:
        print("P")
    elif x>y:
        print("q")
    else:
        print("TIE")