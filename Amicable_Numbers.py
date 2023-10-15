n=int(input())
m=int(input())
i1=0
i2=0
for i in range(1, n):
    if n%i==0:
        i1+=i
for i in range(1, m):
    if  m%i==0:
        i2+=i
if i1==m and i2==n:
    print("Amicable")
else:
    print("Not Amicable")
    