# cook your dish here
t=int(input())
while t>0:
    x,y,z=map(int,input().split())
    t-=1
    if x>y and x>z:
        print("Setter")
    elif y>x and y>z:
        print("Tester")
    else:
        print("Editorialist")