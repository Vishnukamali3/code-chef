# cook your dish here
t=int(input())
k=[]
for i in range(t):
    x=int(input())
    k.append(x)
k.sort()
for i in range(t):
    print(k[i])