# cook your dish here
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    down=n-x
    if n!=x:
        print(min(x,down))
    else:
        print("0")