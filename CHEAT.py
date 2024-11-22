# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    c=0
    for i in range(2,x+1,7):
        c=c+1
    print(c)