# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    avg=0
    total=0
    found=False
    for i in range(n):
        total=total+a[i]
        avg=total/(i+1)
        if avg<40:
            found=True
            print("No")
            break
    if not found:
        print("Yes")