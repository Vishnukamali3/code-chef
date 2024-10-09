t = int(input())

while t > 0:
    x, y, z = map(int, input().split())
    # Your code goes here
    t -= 1
    a=x*5
    b=y*10
    c=a+b
    res=c//z
    print(res)
