"""
N: 듣지도 못한 사람 수 / M: 보지도못한 사람수
"""
n, m = map(int, input().split())

n_set = {input() for _ in range(n)}
m_set = {input() for _ in range(m)}

answer = sorted(n_set & m_set)

print(len(answer))
print('\n'.join(answer))