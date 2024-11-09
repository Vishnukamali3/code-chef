def max_area(n):
    if n<4:
        return 0
    h=n//2
    if h%2==0:
        l=b=h//2
    else:
        l=h//2
        b=(h//2)+1
    return l*b
t=int(input())
for i in range(0,t):
    n=int(input())
    print(max_area(n))