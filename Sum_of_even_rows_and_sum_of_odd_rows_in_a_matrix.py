r,c=map(int,input().split())
mat=[]
for inner_list in range(r):
    inner_list = list(map(int,input().split()))
    mat.append(inner_list)
s1=0
s2=0
for i in range(r):
    for j in range(c):
        if i%2==0:
            s1+=mat[i][j]
        else:
            s2+=mat[i][j]
print(s1, end= ' ')
print(s2)