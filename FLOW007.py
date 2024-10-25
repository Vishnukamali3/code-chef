# cook your dish here
t=int(input())
while t>0:
    x=int(input())
    t-=1
    rev=0
    while x>0:
        rem=x%10
        rev=rev*10+rem
        x=x//10
    print(rev)