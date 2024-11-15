# cook your dish here
t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    x=max(l)
    l.remove(x)
    print(max(l))
    