# cook your dish here
t=int(input())
for i in range(0,t):
    x=int(input())
    if x<3:
        print("LIGHT")
    elif x>=3 and x<7:
        print("MODERATE")
    else:
        print("HEAVY")