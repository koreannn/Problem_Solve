# 문제 이해
# 시작점 (인덱스 0, -1)부분은 물이 차지 않음
# 물이 고이기 위해서는, "현재 위치의 높이 < 양쪽 벽(좌우)의 높이" 이어야 함
# 위 조건(현재 위치의 높이 < 양쪽 벽(좌우)의 높이)을 만족한다고 가정할 때, 각 칸에서 고인 물의 양 = "min(좌측 최대 높이, 우측 최대 높이) - 현재 높이" 로 계산됨
# 위 조건을 만족하지 않으면, 물이 고이지 않음

class Solution:
    def trap(self, height: list[int]) -> int: # <투 포인터 방식> - (시간 복잡도 O(n))
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume
    
    def trap2(self, height: list[int]) -> int: # <브루트 포스 방식> - (시간 복잡도 O(n^2) : 각 칸에 대해서 max()를 호출함)
        n = len(height)
        water = 0
        for i in range(n):
            left_max = max(height[:i+1])
            right_max = max(height[i:])
            water += min(left_max, right_max) - height[i]
        return water 
        # Time Out 발생. 직관적이지만 비효율적
    
    def trap3(self, height: list[int]) -> int: # <DP(동적 계획법)방식> - (시간 복잡도 O(n))
        n = len(height)
        if n == 0:
            return 0
    
        left_max = [0] * n
        right_max = [0] * n
        
        # 1. 좌측 최대 높이 계산
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        # 2. 우측 최대 높이 계산
        right_max[-1] = height[-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        # 물 양 계산
        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]
        return water

# test
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
print(Solution().trap([4,2,0,3,2,5]))  # 9
