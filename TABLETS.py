# cook your dish here
t=int(input())
for i in range(0,t):
    x,y=map(int, input().split())
    a=x*3
    if a<=y:
        print("yes")
    else:
        print("no") 