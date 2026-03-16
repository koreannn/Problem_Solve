"""
먹는다면 가장 먼저나온 햄버거를 먼저 먹어야 한다.
"""

N, K = map(int, input().split()) # 식탁 길이, 햄버거를 선택할수 있는 거리 -> 햄버거 먹을 수 있는 사람의 최대 수
string = input()
answer = 0
eaten_idx_set = set()

for i in range(len(string)):
    if string[i] == 'P':
        for j in range(max(0, i-K), min(N, i+K+1)):
            if string[j] == 'H':
                if j not in eaten_idx_set:
                    eaten_idx_set.add(j)
                    answer += 1
                    break
print(answer)
