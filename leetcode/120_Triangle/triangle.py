"""
- 1레이어는 항상 길이가 1(요소가 무조건 1개)
- 다음 레이어의 요소 개수는 항상 이전 레이어 요소 개수보다 하나 많음
- depth는 1<= <= 200
"""

from types import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        answer = 0
        if not triangle:
            return 0
        
        for i in range(1, len(triangle)):
            # 왼쪽 변
            triangle[i][0] += triangle[i-1][0]
            
            # 오른쪽
            triangle[i][i] += triangle[i-1][i-1]
            
            for j in range(1, i):
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
            
        return min(triangle[-1])
            