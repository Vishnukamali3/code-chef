# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    string=""
    for i in range(len(s)):
        if s[i]=="A":
            string=string+"T"
        elif s[i]=="T":
            string=string+"A"
        elif s[i]=="C":
            string=string+"G"
        elif s[i]=="G":
            string=string+"C"
    print(string)