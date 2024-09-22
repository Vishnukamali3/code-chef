# cook your dish here
def chef(a,b,c):
    x=max(a,b)
    result=x*c
    print(result)
a,b,c=map(int,input().split())
chef(a,b,c)