# cook your dish here
t=int(input())
while t>0:
    n=int(input())
    t-=1
    if n%4==0:
        print("Good")
    else:
        print("Not Good")