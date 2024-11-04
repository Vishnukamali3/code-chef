# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    if n%(k+1)==0:
        print(n//(k+1))
    else:
        a=n//(k+1)
        b=a*k
        print(n-b)
        