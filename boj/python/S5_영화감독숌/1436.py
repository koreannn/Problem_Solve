'''
1: 666
2: 1666
3: 2666
...
6: 5666
7: 6660
8: 6661
9: 6662
10: 6663
...
13: 6666
...
187: 66666
...
500: 166699
...
'''

n = int(input())

target = 666

while(True):
    # target_list = [int(digit) for digit in str(target)]
    # if target_list.count(6)==3:
    if "666" in str(target):
        n -= 1
        if n == 0:
            break
    target+=1
    
print(target)
# print(int(''.join(map(str, target_list))))