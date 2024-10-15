# cook your dish here
t=int(input())
for i in range(t):
    R=list(map(int,input().split()))
    c=0
    for j in range(len(R)):
        if R[j]==1:
            c=c+1
    if c>=4:
        print("YES")
    else:
        print("NO")