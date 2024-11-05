# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a+b%4==0:
        print("Alice")
    else:
        print("BOB")