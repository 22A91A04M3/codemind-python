a,b=map(int,input().split())
if b==a-1 or b==a+1 or a==b-9 or a==b+9:
    (a+b)%2==1
    print("Yes")
else:
    print("No")