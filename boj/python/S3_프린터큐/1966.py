"""
중요도 숫자가 높을수록 중요도가 높음

"""

test_case = int(input())

for _ in range(test_case):
    num_of_docs, query = map(int, input().split()) # 주어지는 문서의 개수, 물어볼 문서의 이름
    score = int(input()) # 'query' 문서의 중요도 점수