# cook your dish here
t=int(input())
for i in range(t):
    a1,a2,b1,b2=map(int,input().split())
    x=(a1-a2)+(b1-b2)
    if x<0:
        print("YES")
    else:
        print("NO")