"""
1. 국어 점수 내림차순
2. (국어 점수가 동일할 경우)영어 점수 오름차순
3. (국어, 영어 점수가 같을 경우)수학 점수 오름차순
4. 모든 점수가 같다면 이름을 사전순으로 (대소문자 구분됨)
"""

N = int(input())
students = []

for _ in range(N):
    name, kor, en, math = map(str, input().split())
    kor = int(kor); en = int(en); math = int(math)
    students.append([name, kor, en, math])

sorted_student = sorted(students, key = lambda x : (-x[1], x[2], -x[3], x[0]),  reverse = False)

print('\n'.join(name[0] for name in sorted_student))