# cook your dish here
t=int(input())
for i in range(t):
    N=int(input())
    if N%4==0:
        print(N//4)
    else:
        print(N//4+1)