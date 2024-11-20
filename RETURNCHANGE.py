# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    b=x//10
    a=x%10
    if a>=5:
        print(100-((b*10)+10))
    else:
        print(100-(b*10))
        