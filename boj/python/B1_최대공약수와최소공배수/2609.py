num1, num2 = map(int, input().split())

denom = max(num1, num2)
mul = 1

while True:
    if num1%denom==0 and num2%denom==0:
        break
    denom -= 1
    
while True:
    if mul%num1==0 and mul%num2==0:
        break
    mul += 1

print(denom)
print(mul)