# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if a<b and a<c:
        print("DRAW")
    elif b<a and b<c:
        print("BOB")
    elif c<a and c<b:
        print("ALICE")