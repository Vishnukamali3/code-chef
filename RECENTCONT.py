# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(str,input().split()))
    s=0
    k=0
    for j in range(n):
        if l[j]=="START38":
            s=s+1
        else:
            k=k+1
    print(s,k)
        