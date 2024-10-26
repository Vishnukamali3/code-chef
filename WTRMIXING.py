# cook your dish here
t=int(input())
for i in range(t):
    n,r,h,c=map(int,input().split())
    if n==r:
        print("YES")
    elif n>r:
        if n-c<=r:
            print("YES")
        else:
            print("No")
    elif n<r:
        if n+h>=r:
            print("YES")
        else:
            print("NO")