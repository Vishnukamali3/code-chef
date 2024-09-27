# cook your dish here
t=int(input())
for i in range(0,t):
    
    a,b,c=map(int,input().split())
    x=a+b
    if x==c:
       print("YES")
    else:
       print("NO")