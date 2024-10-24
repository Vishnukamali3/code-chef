# cook your dish here
t=int(input())
for I in range(t):
    a, b, c=map(int, input().split())
    x=max(a, b, c)
    print(x)