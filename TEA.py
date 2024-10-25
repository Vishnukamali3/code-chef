# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if x==y or x<y:
        print(z)
    elif x>y:
        if x%y==0:
            print((x//y)*z)
        else:
            print((x//y+1)*z)
        