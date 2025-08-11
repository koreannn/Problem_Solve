"""
e.g.

33 시작
33 -> 33+3+3 = 39
39 -> 39+3+9 -> 51
...
33 -> 39 -> 51 -> ... (33은 39의 생성자, 39는 51의 생성자)

셀프 넘버란? 생성자가 없는 숫자
10,000보다 작거나 같은 셀프 넘버를 출력하기
"""

not_self = set() # 셒프 넘버가 아닌 수 모음

curr = 1
while curr <= 10000:
    div = curr
    s = curr    
    while div > 0:
        s += div%10
        div = div//10
    not_self.add(s)
    curr += 1
    
for i in range(1, 10001):
    if i in not_self:
        continue
    print(i)