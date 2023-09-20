n=int(input())
temp = -n if n < 0 else n
reverse = 0
while temp:
    reverse = reverse*10+temp%10
    temp = temp//10
print(-reverse if n < 0 else reverse)