"""
N보다 작거나 같은 모든 소수를 찾는 알고리즘

1. 2부터 N까지 모든 정수를 적는다 -> 2, 3, 4, 5, 6, 7
2. 아직 지우지 않은 정수 중 가장 작은 수를 찾는다. 이 수를 P라고 하고, 이 수는 소수이다.
3. P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
4. 모든 수가 지워지지 않았다면 다시 2번부터 반복한다.

2, 3, 4, 5, 6, 7
2 -> 지우는 수: 2, 4, 6 -> 남은 수: 3, 5, 7
3 -> 지우는 수: 3 -> 남은 수: 5, 7
5 -> 지우는 수: 5 -> 남은 수: 5
7 -> 지우는 수: 7 -> 남은 수: x
"""
N, K = map(int, input().split())
count = 0
nums_check = [True] * (N + 1)

for i in range(2, N+1):
    for curr_num in range(i, N+1, i):
        if nums_check[curr_num]:
            nums_check[curr_num] = False
            count += 1
            if count == K:
                print(curr_num)