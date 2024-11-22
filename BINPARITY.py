# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    re=0
    while x>0:
        re=re+x%2
        x=x//2
    if re%2==0:
        print("EVEN")
    else:
        print("ODD")
        
        