t = int(input())

while t > 0:
    n = int(input())
    h = input()
    # Your code goes here
    t -= 1
    z=""
    for i in range(0,n,2):
        if h[i]+h[i+1]=="00":
            z=z+"A"
        elif h[i]+h[i+1]=="01":
            z=z+"T"
        elif h[i]+h[i+1]=="10":
            z=z+"C"
        else:
            z=z+"G"
    print(z)
