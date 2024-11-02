# cook your dish here
x,y,z=map(int,input().split())
team=x+y*0.5
opponent=z+y*0.5
remaining=4-(x+y+z)
if team+remaining>opponent:
    print("YES")
else:
    print("NO")