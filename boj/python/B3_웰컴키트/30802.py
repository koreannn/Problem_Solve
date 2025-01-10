N = int(input())
size_list = list(map(int, input().split())) # S, M, L, XL, XXL, XXL

T, P = map(int, input().split())


# 첫번쨰줄 출력 : 각 사이즈별로 T장씩 총 몇 묶음 주문해야하는지
t_sum = 0
for size in size_list:
    t_sum += size//T
    if size%T != 0:
        t_sum += 1
print(t_sum)

# 두번째줄 출력 : P자루의 묶음으로 몇 묶음 주문할 수 있고, 1개단위로 몇 자루 주문해야하는지
dozen = N//P
pen = N%P
print(f"{dozen} {pen}")
