# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=list(map(int,input().split()))
    if a!=c and b!=d:
        print("1")
    else:
        print("2")