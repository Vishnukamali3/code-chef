# cook your dish here
t=int(input())
for i in range(0,t):
    n=list(map(int,input().split()))
    n.sort()
    print(n[-2])