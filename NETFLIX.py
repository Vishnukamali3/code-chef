# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,x=map(int,input().split())
    if a+b>=x or a+c>=x or b+c>=x:
        print("YES")
    else:
        print("NO")