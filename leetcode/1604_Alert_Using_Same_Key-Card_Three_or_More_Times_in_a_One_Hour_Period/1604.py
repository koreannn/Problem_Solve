class Solution:
    # e.g.,
    # keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
    # keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
    def time2min(self, time):
        minute =  int(time[:2]) * 60 + int(time[3:])
        return minute
    
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        answer = []
        dict_table = {name: [] for name in keyName}
        
        for i in range(len(keyName)):
            dict_table[keyName[i]].append(keyTime[i])
        
        
        # 출입 시간 정렬
        for person in dict_table.keys():
            dict_table[person].sort()
            
        
        # 찾기
        for person in dict_table.keys():
            curr_person_time_table = dict_table[person]
            
            for i in range(len(curr_person_time_table) - 2):
                if self.time2min(curr_person_time_table[i + 2]) - self.time2min(curr_person_time_table[i]) <= 60:
                    answer.append(person)
                    break
        
        answer.sort()
        return answer

# test
print(Solution().alertNames(keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]))
print(Solution().alertNames(keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]))