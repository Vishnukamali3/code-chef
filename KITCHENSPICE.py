# cook your dish here
t=int(input())
for i in range(0,t):
    x=int(input())
    if x<4:
        print("MILD")
    elif x>=4 and x<7:
        print("MEDIUM")
    else:
        print("HOT")