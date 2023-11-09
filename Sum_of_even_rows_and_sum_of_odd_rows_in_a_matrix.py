r,c = map(int,input().split())
mat = []
for innerlist in range(r):
    innerlist = list(map(int,input().split()))
    mat.append(innerlist)
s=0
s1=0
for i in range(r):
    for j in range(c):
        if i%2==0:
            s=s+mat[i][j]
        else:
            s1=s1+mat[i][j]
print(s,s1)