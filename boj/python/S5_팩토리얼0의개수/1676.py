n = int(input())

count = 0
factorial = 1

for num in range(n, 0, -1):
    factorial = factorial*num
    if (factorial%10 == 0):
        factorial = factorial//10
        count += 1

print(count)