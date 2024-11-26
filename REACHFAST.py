# cook your dish here
t=int(input())
for i in range(t):
    x,y,k=map(int,input().split())
    a=abs(x-y)
    s=(a+k-1)//k
    print(s)