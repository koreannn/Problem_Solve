"""딕셔너리 다루기"""

from collections import Counter

def is_same(num_list: list) -> bool:
    freq = Counter(num_list).values()
    first = list(freq)[0]
    for i in freq:
        if i != first:
            return False
        first = i
    return True
        
def get_freq(num_list: list) -> int:
    counter = Counter(num_list)
    most_common = counter.most_common()
    max_freq = most_common[0][1] 

n = int(input())
num_list = [int(input()) for _ in range(n)]
num_list.sort()

mean_val = round(float(sum(num_list))//len(num_list)) # 산술평균 (반올림)
median_val = num_list[len(num_list)//2] # 중앙값
mode_val = num_list[1] if is_same(num_list) else max(Counter(num_list).values()) # 최빈값 (없을 경우 두 번째로 작은 값)
range_val = num_list[-1] - num_list[0] # 값의 범위

print(mean_val, median_val, mode_val, range_val, sep='\n')

# num_list = [1,2,3,4,5]
# modes = Counter(num_list).values()
# freq = Counter(num_list).values
# num = list(freq)[0]

# print(modes)
