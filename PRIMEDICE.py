# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c=a+b
    cou=0
    for i in range(c):
        if c%i==0:
            cou=cou+1
    if cou==2:
        print("ALICE")
    else:
        print("BOB")
            