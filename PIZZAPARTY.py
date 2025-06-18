# cook your dish here
a,b=list(map(int,input().split()))
x=(a+1)*4
y=b*3
z=x+y
if z%8==0:
    print(z//8)
else:
    print((z//8)+1)