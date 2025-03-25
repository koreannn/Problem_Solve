"""
열: 0, 1 -> 4, 5 -> 16(2^4), 17, -> 20(2^4+2^2), 21 -> 64(2^8), 65
행: 0, 2 -> 8(0+2^3), 10(2+2^3) -> 32(2^3*2^2), 34(2^3*2^2+2) -> 40(32+2^3), 42(34+2^3)
    0, 2, 4, 6, 8 .. : 0, 0+2^3, (2^3)*2^2 / 32+2^3, 40*2^2 => x0, x1=x0+2^3, 
    1, 3, 5, 7, 9 .. : 2, 2+2^3, 2+2^3*2^2 / 34+2^3, 34+2^2*2^2 => 

"""
# N, r, c = map(int, input().split())
# answer = 0

# row_start=0
# for i in range(r//2):
#     if (i//2)%2 == 0: # i=0 / 2,3 / 6,7 / 10, 11 / ... / 
#         row_start += 8
#     else: # i=1 / 4,5 / 8,9 / 12, 13 / ... / 
#         row_start *= 4
# if r%2 != 0:
#     row_start+=2

def solution(N, r, c):
    if N==0:
        return 0
    
    half = 2**(N-1)
    if r < half and c < half:
        return solution(N-1, r, c)
    elif r < half and c >= half:
        return half * half + solution(N-1, r, c-half)
    elif r >= half and c < half:
        return 2 * half * half + solution(N-1, r-half, c)
    else:
        return 3 * half * half + solution(N-1, r-half, c-half)

N, r, c = map(int, input().split())
print(solution(N, r, c))