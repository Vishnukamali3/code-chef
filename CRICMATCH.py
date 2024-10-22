# cook your dish here
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    balls=6*m
    runs=balls*6
    if n<=runs:
        print("yes")
    else:
        print("NO")
        