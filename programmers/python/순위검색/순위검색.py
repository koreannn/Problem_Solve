def solution(info, query):
    answer = []
    sorted_info = sorted(info, key=lambda x: int(x.split()[-1]), reverse=True)
    
    for i in range(len(query)):
        curr_answer = 0
        test_pass = [] # 쿼리 별 코딩테스트 합격자만 담는 리스트
        
        # 코테 점수 미달 시 바로 다음 쿼리로 넘어가기
        for j in range(len(info)):
            if int(query[i].split()[-1]) < int(sorted_info[i].split()[-1]):
                test_pass.append(info[j])
            
        criteria = 0
        for segment_query in query[i].split("and"):
            checked = True
            
            for info in test_pass: # 코테 합격자 내에서 탐색
                if segment_query.strip() == info.split()[criteria] or segment_query.strip() == '-':
                    criteria += 1
                    continue
                else:
                    checked = False
                    break
            
            if not checked: # 기준을 모두 충족하는 경우
                curr_answer += 1
            
        answer.append(curr_answer)
    
    return answer


"""
info 예시
"java backend junior pizza 150"
"python frontend senior chicken 210"
"python frontend senior chicken 150"
"cpp backend senior pizza 260"
"java backend junior chicken 80"
"python backend senior chicken 50"
→ "언어 프론트/백 시니어/주니어 소울프드 코테점수" 형태

query 예시
"java and backend and junior and pizza 100"
"python and frontend and senior and chicken 200"
"cpp and - and senior and pizza 250"
"- and backend and senior and - 150"
"- and - and - and chicken 100"
"- and - and - and - 150"
→ "- and - and - and - 코테점수" 형태
"""

# test
informations = ["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"]

queries = ["java and backend and junior and pizza 100",
            "python and frontend and senior and chicken 200",
            "cpp and - and senior and pizza 250",
            "- and backend and senior and - 150",
            "- and - and - and chicken 100",
            "- and - and - and - 150"]

print(solution(informations, queries)) # [1,1,1,1,2,4]