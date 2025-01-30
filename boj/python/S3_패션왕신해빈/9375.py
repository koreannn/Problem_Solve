test_case = int(input()) # <=100
answer = []

for i in range(test_case):
    # count = 0
    # prod = 1
    n = int(input()) # 0 <= n <= 30
    cloth_dict = {}
    
    for l in range(n):
        name, kind = input().split()
        # if kind not in cloth_dict.keys(): # 리스트 타입으로 반환
        if kind not in cloth_dict: 
            cloth_dict[kind] = []
        cloth_dict[kind].append(name)
    
    prod = 1
    for cloth in cloth_dict.keys():
        prod *= (len(cloth_dict[cloth]) + 1) # 각 종류에서 안입는 경우도 추가 (+1)
    
    answer.append(prod-1) # 아예 아무것도 안입는 경우는 빼주기 (-1)
    # if len(cloth_dict.keys()) < 2: # 한 종류만 있을 경우
    #     count += len(cloth_dict[kind])
    #     answer.append((count))
    # else:
    #     for cloth in cloth_dict.keys(): # 두 종류 이상일 경우
    #         count += len(cloth_dict[cloth])
    #         prod *= len(cloth_dict[cloth])
    #     answer.append((count+prod))

for num in answer:
    print(num)

'''
<시간복잡도 비교>
기존:
for cloth in cloth_dict.keys(): # O(K), K는 옷 종류의 개수
    count += len(cloth_dict[cloth]) # O(1)*K
    prod *= len(cloth_dict[cloth]) # O(1)*K
최종적으로, O(K+K)

수정:
for cloth in cloth_dict.keys():
    prod *= (len(cloth_dict[cloth]) + 1) # O(1)*K
최종적으로, O(K)

두 배 차이.
'''