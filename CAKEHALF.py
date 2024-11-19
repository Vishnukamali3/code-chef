# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    s=0
    while x!=y:
        if x>y:
            if x%2==0:
                s=s+(x//2)
                x=x//2
            else:
                s=s+((x+1)//2)
                x=x//2
        elif y>x:
            if y%2==0:
                s=s+(y//2)
                y=y//2
            else:
                s=s+((y+1)//2)
                y=y//2
    print(s)