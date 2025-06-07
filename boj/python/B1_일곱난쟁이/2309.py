from itertools import combinations

heights = [int(input()) for _ in range(9)]
total = sum(heights)

for a, b in combinations(heights, 2): # 9명 중 2명을 뽑아서 제거해봄
    if total - a - b == 100:
        heights.remove(a)
        heights.remove(b)
        break

for h in sorted(heights):
    print(h)