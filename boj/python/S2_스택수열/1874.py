"""
e.g. n=8
4 3 6 8 7 5 2 1 
1 2 3 4 5 6 7 8 순서대로 push

stack.append(1)
if 1 == 4:
    stack.pop()
1 != 4 -> stack.append(1)
2 != 4 -> stack.append(2)
3 != 4 -> stack.append(3)
4 == 4 -> 
"""
import sys

input = sys.stdin.readline

n = int(input().strip()) # 1<= n <= 100000
stack = []
nums = []
answer = []
curr = 1

for _ in range(n):
    num = int(input().strip())
    nums.append(num)

for target in nums:
    while curr <= target:
        stack.append(curr)
        answer.append("+")
        curr += 1
    
    if stack and stack[-1] == target:
        stack.pop()
        answer.append("-")
    else:
        answer.clear()
        answer.append("NO")
        break

print("\n".join(answer))

