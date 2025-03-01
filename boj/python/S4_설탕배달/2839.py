N = int(input()) # 3<=N<=5000

answer = -1

for i in range(N//5, -1, -1):
    remain = N - (5*i) # 일단 5로 최대한 나눠보기
    if remain % 3 == 0: # 3으로 나누어 떨어지면, 그게 정답임
        answer = i + (remain//3)
        break

print(answer)