from collections import deque

N = int(input())

cards = deque([num for num in range(1, N+1)])

while len(cards) != 1:
    cards.popleft()
    append_num = cards.popleft()
    cards.append(append_num)

print(cards[0])