"""
N = 1 -> 1 (1)
N = 2 -> 00, 11 (2)
N = 3 -> 001, 100, 111 (3)
N = 4 -> 0000, 0011, 1001, 1100, 1111 (5)
N = 5 -> 00001, 00100, 10000, 00111, 10011, 11001, 11100, 11111 (8)
N = 6 -> 000000 / 000011, 001001, 001100, 100100, 110000, 100001 / 001111, 100111, 110011, 111001, 111100 / 111111 (13)

e.g. N = 6
00이 0개 -> 6!/6! (1)
00이 1개 -> 5!/4!1! (5)
00이 2개 -> 4!/2!2! (6)
00이 3개 -> 3!/3!
"""
N = int(input()) # 1~1,000,000

dp = [0]*(N+2)

dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746 # 값이 너무 커질 경우(e.g. N = 백만)메모리 초과를 방지하기 위한 임의 수

print(dp[N])

# 시간복잡도 O(N^2) ~ O(N^3)
# N = int(input()) # 1~1,000,000

# def factorial(num: int) -> int:
#     if num <= 1:
#         return 1
#     else:
#         return num*factorial(num-1)

# num_of_zero_tile = 0
# answer = 0

# while N - num_of_zero_tile * 2 >= 0:
#     one_tile = N - num_of_zero_tile * 2
#     answer += factorial(one_tile + num_of_zero_tile) // (factorial(one_tile) * factorial(num_of_zero_tile))
#     num_of_zero_tile += 1

# print(answer)