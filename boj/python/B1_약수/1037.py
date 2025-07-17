import sys
from math import lcm
input = sys.stdin.readline

num_of_real_div = int(input()) # 진짜 약수의 개수
real_div = map(int, input().split()) # '진짜 약수'들
sorted_real_div = sorted(real_div)
answer = 0

"""real_div들의 최소공배수 구하기"""
# 1. 라이브러리 활용
answer = lcm(*sorted_real_div)

# # 2. sorted_real_div의 최솟값*최댓값 = 최소공배수
# answer = sorted_real_div[0] * sorted_real_div[-1]

print(answer)