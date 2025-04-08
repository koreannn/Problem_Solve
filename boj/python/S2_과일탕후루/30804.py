from collections import defaultdict

n = int(input())
fruits = list(map(int, input().split()))

max_len = 0
basket = defaultdict(int)
left = 0

for right in range(n):
    basket[fruits[right]] += 1
    
    while len(basket) > 2: # 두 종류가 넘어가면 left값 조정
        basket[fruits[left]] -= 1
        if basket[fruits[left]] == 0:
            del basket[fruits[left]]
        left += 1
    
    max_len = max(max_len, right-left+1)

print(max_len)