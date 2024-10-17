# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    wealth=l[-1]
    pos=n-1
    for j in range(n-2,-1,-1):
        if l[j]<=(wealth//2):
            pos-=1
        else:
            break;
    print(pos+1)