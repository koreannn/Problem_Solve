m, n = map(int, input().split()) # 1<= n, m <= 1,000,000
answer = []

def is_prime(num: int) -> bool:
    answer = False
    for i in range(2, num):
        if num%i == 0:
            return answer
    answer = True
    return answer

for num in range(n, m+1):
    if num == 1:
        answer.append(str(num))
        continue
    if is_prime(num):
        answer.append(str(num))

print(answer)
print("\n".join(answer))