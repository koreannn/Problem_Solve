s = input().strip().upper()
count = {}

for char in s:
    count[char] = count.get(char, 0)+1
    
max_count = max(count.values())
candidates = [k for k, v in count.items() if v == max_count]

if len(candidates) > 1:
    print("?")
else:
    print(candidates[0])