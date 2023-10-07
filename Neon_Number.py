n=int(input())
sq=n*n
q=0
s=0
while(sq!=0):
    q=sq%10
    sq=sq//10
    s=q+s
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")