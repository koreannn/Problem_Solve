import heapq
import sys
input = sys.stdin.readline

N = int(input().strip())
heap = []
for _ in range(N):
    num = int(input().strip())
    if num == 0:
        if heap: # 힙이 비어있지 않을 경우 최소값을 출력
            print(heapq.heappop(heap))
        else: # 힙이 비어있으면 0 출력
            print(0)
    else: # num이 자연수이면 힙에 추가
        heapq.heappush(heap, num)