# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    a=z*2+x
    if a>=y:
        print("YES")
    else:
        print("NO")