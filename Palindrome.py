n=int(input())
r=0
s=0
q=n
while(n!=0):
    r=n%10
    n=n//10
    s=(s*10)+r
if s==q:
    print("True")
else:
    print("False")