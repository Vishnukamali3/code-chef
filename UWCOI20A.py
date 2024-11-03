# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    maxi=s[0]
    for i in range(1,len(s)):
        if s[i]>maxi:
            maxi=s[i]
    print(maxi)