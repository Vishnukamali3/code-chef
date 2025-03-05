# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    x=2*(a*b+b*c+c*a)
    print(1000//x)