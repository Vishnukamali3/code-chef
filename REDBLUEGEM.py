# cook your dish here
r,b,p,q=list(map(int,input().split()))
a=r*p
b=b*q
if a>b:
    print(a)
else:
    print(b)