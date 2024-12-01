# cook your dish here
t=int(input())
for i in range(t):
    s=input()
    n=input()
    ans=""
    for i in range(len(s)):
        if s[i]==n[i]:
            ans=ans+"G"
        else:
            ans=ans+"B"
    print(ans)