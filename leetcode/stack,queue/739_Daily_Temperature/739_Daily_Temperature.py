# 반복문 돌면서 해당 지점에서 얼만큼 더 지나야 따뜻한 날이 오는지 (지난날은x, 앞으로 남은 날 중 가장 가까운날)
class Solution:
    def dailyTemperatures1(self, temperatures: list[int]) -> list[int]: # 시간 복잡도 줄여야함
        answer = []
        
        for i in range(len(temperatures)): 
            find = False
            for l in range(i, len(temperatures)):
                if temperatures[i] < temperatures[l]:
                    find = True
                    answer.append(l-i)
                    break
                # answer.append(0) # -> 이렇게 작성하면 조건문 만족 못할때마다 0을 append
            if not find:
                answer.append(0)
        return answer
        
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = []
        
# test
print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])) # [1,1,4,2,1,1,0,0]