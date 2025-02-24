# 두 개 이상의 연산자가 연속으로 등장하는경우 X (연산자는 +, - 두 개 뿐임)
# 다섯자리 이하의 수
# 숫자는 0으로 시작할 수 있음
# 수식의 총 길이: 50이하
# 첫 - 뒤에 나오는 숫자를 최대한 크게 만들자? X -> -가 나올때마다 더해지는 숫자들의 합은 괄호로 묶어서 계산해야함

mod = input()
result = 0

vals = mod.split('-')
# result = eval(vals[0]) # 가장 앞에 있는 수식 (초기값)
result = sum(map(int, vals[0].split('+')))

for i in range(1, len(vals)):
    # result -= eval(vals[i])
    result -= sum(map(int, vals[i].split('+')))

print(result)