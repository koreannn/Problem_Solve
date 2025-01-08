'''
카드의 합을 최대한 크게 만들기(21이하로)
-> 카드 N장을 모두 보이도록 놓음 -> 제한시간 내로 N장의 카드 중 숫자 M(딜러가 외친 숫자)과 가장 가까우면서 넘지 않는 수를 만들어야함
-> 즉, N장 중 3장을 뽑아 M과 가장 가까우면서 이하인 수 만들기

N, M을 입력받는다.
숫자열을 입력받는다.
숫자열 3개를 조합했을 때 M과 가장 가까운 수가 무엇인지 출력한다. (입력은 M을 넘지않는 카드 3장을 무조건 찾을 수 있는 입력값으로 가정한다)
'''
from itertools import combinations

max_sum = 0
N, M = map(int, input().split())

num_list = list(map(int, input().split()))

for comb in combinations(num_list, 3):
    iter_sum = sum(comb)
    if iter_sum <= M:
        max_sum = max(iter_sum, max_sum)
    
print(max_sum)
