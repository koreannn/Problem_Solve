"""
기본 요금: 5000원, 180분
단위 요금: 600원, 10분
하루 단위 요금(23:59까지의 요금을 계산)

- 첫 번째 반복문: records 원소들을 순차적으로 iter
    - 입차 시 딕셔너리에 집어넣기 (차량 번호: 입차시간) 꼴로 -> 출차 시 딕셔너리에서 빼기(반복)
    - 반복문 종료 후 딕셔너리에 남아있는 원소에 대해서는 23:59를 출차 시간으로 간주하기
- 시간을 분으로 변환하는 함수?

"""

def solution(fees, records):
    answer = []
    answer_dict = {} # 차량별 총 주차 분 수를 저장하는 딕셔너리 / e.g. {'5503': 3560} 
    
    # {차량번호: 전체 시간} 꼴로 저장 & 전체 시간: 24시간을 기준으로 전부 분단위로
    # e.g. 5503차량 13:05분 입차 -> {'5503': 13*60+05}
    table = {} 
    for rec in records:
        time, car_num, in_out = rec.split()
        
        if in_out == "IN": # 입차일 경우
            in_hour, in_minute = map(int, time.split(':'))
            table[car_num] = in_hour*60 + in_minute
        
        else: # 출차일 경우(in_out == "OUT")
            # in_hour, in_minute = map(int, table[car_num].split(':'))
            out_hour, out_minute = map(int, time.split(':'))
            total_minute = (out_hour*60 + out_minute) - table[car_num]
            
            if car_num in answer_dict: # 두 번 이상 입차한 경우
                answer_dict[car_num] += total_minute
            else: # 처음이었을 경우
                answer_dict[car_num] = total_minute
            
            del table[car_num]
            
    # 23:59를 출차 시간으로 잡아야하는 차가 있을 경우를 계산
    # 입차 후 출차 기록이 없는 경우
    if table:
        day_finish = 23*60 + 59 # 23시 59분의 분
        for carnum, minute in zip(table.keys(), table.values()):
            if carnum in answer_dict:
                answer_dict[carnum] += (day_finish - minute)
            else:
                answer_dict[carnum] = day_finish - minute
    
    
    # 분 -> 요금으로 변환
    sorted_dict = {k: answer_dict[k] for k in sorted(answer_dict)}
    times = sorted_dict.values() # 각 차량의 전체 분 수
    for m in times:
        if m < fees[0]: # 기본 시간보다 조금 있었을 경우
            fee = fees[1]
            answer.append(fee)
        else: # 기본 요금 + 추가 요금
            fee = fees[1]
            additonal_fee = int(((m - fees[0])/fees[2])) if ((m - fees[0])/fees[2]) == int((m - fees[0])/fees[2]) else int((m - fees[0])/fees[2]) + 1
            fee += additonal_fee*fees[-1]
            answer.append(fee)
        
    return answer


# test
fees_1 = [180, 5000, 10, 600] # 각각 [기본 시간, 기본 요금, 단위 시간, 단위 요금]
records_1 = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees_1, records_1)) # [14600, 34400, 5000]

fees_2 = [120, 0, 60, 591]
records_2 = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
print(solution(fees_2, records_2))

fees_3 = [1, 461, 1, 10]
records_3 = ["00:00 1234 IN"]
print(solution(fees_3, records_3))
