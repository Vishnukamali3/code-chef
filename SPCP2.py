# cook your dish here
t=int(input())
for i in range(t):
    x,n=map(int,input().split())
    a=x*100
    if a<n:
        b=n-a
        if b%100==0:
            print(b//100)
        else:
            print((b//100)+1)
    else:
        print("0")