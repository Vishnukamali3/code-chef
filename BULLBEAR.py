# cook your dish here
def profit():
    t=int(input())
    for i in range(0,t):
        x,y=map(int,input().split())
        if y>x:
            print("PROFIT")
        elif y==x:
            print("NEUTRAL")
        else:
            print("LOSS")
profit()
            