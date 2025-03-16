"""
도시 크기: NxN
(r,c) = r행 c열 (1부터 시작)
0: 빈칸, 1: 집, 2: 치킨집
다 돌아보고, 치킨거리가 가장 작은 순서대로 answer를 만들고, 값을 담기만 하면 된다
"""

import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
chicken_point = []
house_point = []
chicken_distance = []

city = []
for i in range(N):
    row = list(map(int, input().split()))
    city.append(row)
    for j in range(N):
        if row[j] == 2:
            chicken_point.append((i+1, j+1))
        if row[j] == 1:
            house_point.append((i+1, j+1))

def get_chicken_distance(houses, selected_chickens):
    total_distance = 0
    for house in houses:
        min_distance = float('inf')
        for chicken in selected_chickens:
            distance = abs(house[0]-chicken[0]) + abs(house[1]-chicken[1])
            min_distance = min(distance, min_distance)
        total_distance += min_distance
    return total_distance # 각 집들의 치킨거리의 합 (= 도시의 치킨 거리)

min_total_distance = float('inf')
for selected_chickens in combinations(chicken_point, M):
    distance = get_chicken_distance(house_point, selected_chickens)
    min_total_distance = min(min_total_distance, distance)

print(min_total_distance)