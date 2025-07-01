def binary_translate(num: int, length: int) -> str:
    binary = []
    
    curr = length
    while num > 0:
        div=2**(curr-1)
        binary.append(str(num//div))
        num = num%div
        curr -= 1
        
    if len(binary) < length:
        for _ in range(length - len(binary)):
            binary.append('0')
            
    return ''.join(binary)


def check_continuous(num_string: str) -> bool:
    check = False
    curr = num_string[0]
    for i in range(1, len(num_string)):
        if num_string[i] == curr and num_string[i] == '1':
            check = True
            return check
        curr = num_string[i]
    
    return check


n = int(input())
answer = 0

for num in range(1, 2**n): # e.g. n=3 -> 1, 2, 3, 4, 5, 6, 7
    curr = binary_translate(num, n)
    if (curr[0] == '0') or curr == check_continuous(curr):
        continue
    answer += 1
        
print(answer)