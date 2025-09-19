"""
n이 주졌을 때, n에 대한 퍼펙트 스퀘어의 최소값을 리턴하라. (1<= n <= 10000)

퍼펙트 스퀘어란? 

e.g. 
n = 12
12 -> 4 + 4 + 4 (output = 3)

n = 13
13 -> 9 + 4 (output = 2)

1 -> 1
2 -> 1+1
3 -> 1+1+1

4 -> 4
5 -> 4+1
6 -> 4+1+1
7 -> 4+1+1+1
8 -> 4+4

9 -> 9
10 -> 9+1
11 -> 9+1+1

12 -> 4+4+4

13 -> 9+4
14 -> 9+4+1
15 -> 
"""
class Solution():
    def numSquares(self, n: int) -> int:
        answer = 0
        
        squares = []
        for i in range(1, n+1):
            squares.append(i**2)
        
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        
        for i in range(1, n+1):
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        answer = dp[n]
        
        return answer

# test
print(Solution.numSquares(12)) # 3
print(Solution.numSquares(13)) # 2