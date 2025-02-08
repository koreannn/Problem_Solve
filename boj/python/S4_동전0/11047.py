# 동전의 종류, 만들어야하는 가치의 합
N, K = map(int, input().split())
price_list = []
answer = 0

for _ in range(N):
    price_list.append(int(input()))

price_list.sort(reverse=True)

for price in price_list:
    if K//price != 0:
        answer += K//price
        K %= price

print(answer)

