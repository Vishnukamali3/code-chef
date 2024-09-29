# cook your dish here
def alice():
    t=int(input())
    for i in range(0,t):
        a,b,c=map(int,input().split())
        if a>b and a>c:
            print("Alice")
        elif b>a and b>c:
            print("Bob")
        elif c>a and c>b:
            print("Charlie")
alice()