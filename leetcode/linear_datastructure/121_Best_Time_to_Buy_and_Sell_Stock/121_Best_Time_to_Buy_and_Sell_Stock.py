from collections import deque
# 저점 매수 -> 고점 매도 값

class Solution:
    def maxProfit(self, prices: list[int]) -> int: # 시간 초과 (시간 복잡도 : O(n^2))
        curr_queue = deque(prices)
        
        max_profit = 0
        for i in range(len(prices)-1):
            curr_queue.popleft()
            if max(list(curr_queue)) - prices[i] > max_profit:
                max_profit = max(list(curr_queue)) - prices[i]
        return max_profit
    
    def maxProfit2(self, prices: list[int]) -> int:
        min_price = max(prices)
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price) # 일단 사
            max_profit = max(max_profit, price-min_price) # 매번 차익을 계산 -> 최종적으로 가장 큰 차익을 저장해두게 됨
            
        return max_profit
# test
print(Solution().maxProfit([7,1,5,3,6,4])) # 5
print(Solution().maxProfit([7,6,4,3,1])) # 0