N, M = map(int, input().split()) # 포켓몬 도감에 수록되어있는 포켓몬의 수, 맞춰야하는 문제의 수
poketmon_list = ['0']*(N+1)
problem = ['0']*(M+1)
answer = []

'''
모두 영어로만 이루어짐
첫글자만 대문자로 이루어짐 (일부 포켓몬은 마지막 글자만 대문자일수도 있음)
2 <= 포켓몬 이름의 길이 <= 20
M개의 줄에 걸쳐 
    숫자가 들어올 경우, 해당 숫자에 해당하는 포켓몬의 이름을 출력
    문자가 들어올 경우, 해당 문자에 해당하는 포켓몬의 숫자를 출력
'''

for i in range(1, N+1): # 1번 인덱스 ~ N번 인덱스
    poketmon_list[i] = input()

for i in range(1, M+1):
    problem[i] = input()

for i in range(1, M+1):
    if problem[i].isdigit(): # 숫자일 경우
        answer.append(poketmon_list[int(problem[i])])
    else: # 문자일 경우
        answer.append(str(poketmon_list.index(problem[i])))

print('\n'.join(answer))
