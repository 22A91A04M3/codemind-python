n=int(input())
sq1=n*n
s1=0
s2=0
r=0
while(n!=0):
    r=n%10
    n=n//10
    s1=(s1*10)+r
    sq2=s1*s1
while(sq2!=0):
    r=sq2%10
    sq2=sq2//10
    s2=(s2*10)+r
if s2==sq1:
    print("True")
else:
    print("False")
    