# cook your dish here
def chocolate(c,x,y):
    need=c-x
    total=need*y
    print(total)
t=int(input())
for i in range(t):
    c,x,y=map(int,input().split())
    chocolate(c,x,y)