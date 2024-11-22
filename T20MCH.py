# cook your dish here
r,o,c=map(int,input().split())
over=20-o
get=over*6
sc=get*6
mx=c+sc
if mx>r:
    print("YES")
else:
    print("NO")