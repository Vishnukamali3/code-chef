# cook your dish here
t=int(input())
for i in range(t):
    w,x,y,z=map(int,input().split())
    if w==x or w==y or w==z:
        print("YES")
    elif w==x+y or w==y+z or w==x+z:
        print("YES")
    elif w==x+y+z:
        print("YES")
    else:
        print("NO")