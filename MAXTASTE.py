# cook your dish here
t=int(input())
for I in range(t):
    a, b, c, d=map(int, input().split())
    x=max(a, b)
    y=max(c, d)
    print(x+y)