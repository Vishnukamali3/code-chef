# cook your dish here
a,b,c,x=map(int,input().split())
cuboid=a*b*c
cube=x*x*x
if cuboid>cube:
    print("Cuboid")
elif cube>cuboid:
    print("Cube")
else:
    print("Equal")