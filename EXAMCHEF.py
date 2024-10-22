# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    k=x*y
    p=(z/k)*100
    if p>50:
        print("yes")
    else:
        print("NO")