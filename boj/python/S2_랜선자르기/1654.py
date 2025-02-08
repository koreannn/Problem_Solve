# 가장 긴 길이이면서 개수 맞춰 만들어야 함
# 802 + 743 + 457 + 539 = 2541 -> 11개 :  231cm >> 그리디
K, N = map(int, input().split()) # K : 이미 가지고있는 랜선 개수 / N : 필요한 랜선의 개수
wire_list = []
for _ in range(K):
    wire_list.append(int(input()))
    
max_len = sum(wire_list)//len(wire_list)

while(1):
    for num in wire_list:
        count = 0
        count += num//max_len
    if count < N:
        max_len -= 1
    else:
        break
    
print(max_len)