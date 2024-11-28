# cook your dish here
x,y,z=map(int,input().split())
a=y*z
if a<=x:
    print(x-a)
else:
    print("-1")