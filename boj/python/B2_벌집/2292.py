# 1 -> answer=2 : 2~7 (6개) -> answer=3 : 8~19 (6*2개) -> answer=4 : 20~37(6*3개) -> answer=5 : 38~61(6*4개)


def solution():
    layer = 1
    target = int(input())
    answer = 1

    while target > answer:
        answer += 6*layer
        layer += 1
    return layer

print(solution())
