is_same = set()
answer = 0

for _ in range(10):
    num = int(input())
    is_same.add(num%42)
    
answer = len(is_same)
print(answer)