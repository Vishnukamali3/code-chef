t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    # Your code goes here
    t -= 1
    if a==b or b==c or c==a:
        print("NO")
    else:
        print("YES")