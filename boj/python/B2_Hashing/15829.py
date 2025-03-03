# print(ord('a')) # 97

L = int(input())
S = input()
answer = 0
exponent = 0

for char in S:
    answer += (ord(char)-96)*(31**exponent)
    exponent+=1

print(answer%1234567891)
