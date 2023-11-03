r,c = map(int,input().split())
mat = []
for i in range(r):
    inner_list = list(map(int,input().split()))
    mat.append(inner_list)
s1=0
s2=0
for inner_list in mat:
    for every_value in inner_list:
        if every_value%2==0:
            s1 += every_value
        else:
            s2 += every_value
print(s1, end = ' ')
print(s2)
    