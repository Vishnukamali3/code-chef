t = int(input())

while t > 0:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Your code goes here
    t -= 1
    tot=0
    for i in range(n):
        if a[i]>=x:
            tot=tot+b[i]
    print(tot)
