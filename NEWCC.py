# cook your dish here
x,y=map(int,input().split())
if x>y:
    print("NEW")
elif y>x:
    print("OLD")
else:
    print("SAME")