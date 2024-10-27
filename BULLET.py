# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    a=y//x
    if a<z:
        print(z-a)
    else:
        print("0")