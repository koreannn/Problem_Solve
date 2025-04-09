"""
4개 이하의 자연수 제곱합으로 만들 수 있음
1<= n <= 50,000

1 = 1^2
2 = 1^2 + 1^2
3 = 1^2 + 1^2 + 1^2
4 = 2^2
5 = 2^2 + 1^2
6 = 2^2 + 1^2 + 1^2
7 = 2^2 + 1^2 + 1^2 + 1^2
"""
n = int(input())
answer_list = [float('inf')]*(n+1)
answer_list[0] = 0

for i in range(1, n+1):
    j = 1
    while j**2 <= i:
        answer_list[i] = min(answer_list[i], answer_list[i-j**2]+1)
        j += 1
    print(j**2)

print(answer_list[n])