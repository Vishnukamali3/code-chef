# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if z>=x+y:
        print("2")
    elif z>=x:
        print("1")
    else:
        print("0")
    