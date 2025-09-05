"""
1개 쓸 떄 -> arr[1]
2개 쓸 떄 -> 1개쓸 떄 or 2개 쓸 때 비교
3개 쓸 떄 -> 2개 쓸 때 or 3개 쓸 떄 비교
4개 쓸 떄 -> ...

3개 쓸 떄 비교 수식: answer[2] or arr[3]*3 
"""

n = int(input())
answer = [0]*(n+1) # e.g. answer[3]: 로프 3개를 쓸때 들 수 있는 최대 무게
lopes = [0]*n

for i in range(n):
    lope = int(input())
    lopes[i] = lope
sorted_lopes = [0] + sorted(lopes, reverse=True)

answer[1] = sorted_lopes[1]

for i in range(2, n+1):
    answer[i] = max(sorted_lopes[i] * i, answer[i-1]) # 더 조금 버틸 수 있는거까지 써서 or 더 많이 버티는거 하나만 써서

print(answer[n])
