n=int(input())
m = 0
while n:
    c = n%10
    if c>m:
        m=c
    n=n//10
print(m)