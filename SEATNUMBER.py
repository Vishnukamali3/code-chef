# cook your dish here
t=int(input())
for I in range(t):
    x=int(input())
    if x>=1 and x<=10:
        print("lower double")
    elif x>=11 and x<=15:
        print("lower single")
    elif x>=16 and x<=25:
        print("upper double")
    else:
        print("upper single")