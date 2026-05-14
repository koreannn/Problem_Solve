N, K, M = map(int, input().split()) # 보급품 개수, 신입사원 수, 각 가방에 담을 수 있는 최대 무게

for _ in range(N):
    weight, value = map(int, input().split()) # 보급품의 무게, 가치