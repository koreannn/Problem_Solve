from collections import deque

n, k = map(int, input().split())
person_list = [num for num in range(1, n+1)]
person_deque = deque(person_list)
answer = []

while person_deque:
    person_deque.rotate(-(k-1))
    curr = person_deque.popleft()
    answer.append(str(curr))

print("<" + ', '.join(answer) + ">")