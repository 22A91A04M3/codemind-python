n=int(input())
i=n%10
n=n//10
t=n%10
n=n//10
s=n%10
n=n//10
f=n%10
n=n//10
if f==6:
    f=9
elif s==6:
    s=9
elif t==6:
    t=9
else:
    i=9
print(f,s,t,i, sep='')