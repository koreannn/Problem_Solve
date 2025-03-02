T = int(input())  # 테스트 케이스 개수
answer = []

# dp[i] = (i를 호출할 때 0의 호출 횟수, 1의 호출 횟수)
dp = [(1, 0), (0, 1)]  # 초기값(fibonacci(0), fibonacci(1)에서의 0, 1개수)

for i in range(2, 41):
    # i번째 피보나치 수의 0,1 호출 횟수는 i-1번째와 i-2번째 호출 횟수의 합
    zero = dp[i-1][0] + dp[i-2][0]
    one = dp[i-1][1] + dp[i-2][1]
    dp.append((zero, one))

for _ in range(T):
    n = int(input())
    answer.append(dp[n])

for zero, one in answer:
    print(zero, one)

'''
e.g. 3-> 1, 2 
3 -> fibo(2) + fibo(1) -> (fibo(1)+fibo(0)) + fibo(1)
'''