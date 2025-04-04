'''
1과 2로 n을 만들 수 있는 경우의 수 & 둘 중 큰 값으로 콤비네이션값 계산 (e.g 1이 3, 2가 5 -> 5C3)
'''
import math

n = int(input()) # 1>=, <= 1000
answer = 0
num_of_1 = 0
num_of_2 = 0

while n-2*num_of_2 >= 0:
    num_of_1 = n-2*num_of_2
    total_files = num_of_1 + num_of_2
    answer += math.comb(total_files, num_of_2)
    
    num_of_2 += 1
    # answer += math.comb(max(num_of_1, num_of_2)+1, min(num_of_1, num_of_2)) 
    # 끼워넣기 -> 사이에 하나의 타일만 끼워넣을 수 있다는 제약이 생김

print(answer%10007)