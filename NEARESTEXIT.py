# cook your dish here
t=int(input())
while t>0:
    x=int(input())
    t-=1
    if x<=50:
        print("LEFT")
    else:
        print("RIGHT")