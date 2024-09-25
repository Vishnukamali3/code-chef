# cook your dish here
def dollar():
    t=int(input())
    for i in range(0,t):
        x,y=map(int,input().split())
        if y<=x:
            print("YES")
        else:
            print("NO")
dollar()