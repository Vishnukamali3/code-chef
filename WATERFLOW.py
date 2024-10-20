# cook your dish here
t=int(input())
for i in range(t):
    def water():
        w,x,y,z=map(int,input().split())
        avi=x-w
        a=w+(y*z)
        if a>x:
            print("OverFlow")
        elif a==x:
            print("FILLED")
        else:
            print("Unfilled")
    water()