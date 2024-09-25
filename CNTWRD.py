# cook your dish here
def book():
    t=int(input())
    for i in range(0,t):
        m,n=map(int,input().split())
        print(m*n)
book()