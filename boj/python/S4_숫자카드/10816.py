from collections import Counter

n = int(input()) # 1<= n <= 500,000
n_list = map(int, input().split())
m = int(input()) # 1<= m <= 500,000
m_list = map(int, input().split())

counter = Counter(n_list)
# print(counter)
answer_list = []

for num in m_list:
    answer_list.append(str(counter[num]))

print('\n'.join(answer_list))