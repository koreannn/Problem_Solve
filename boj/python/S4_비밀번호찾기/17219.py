N, M = map(int, input().split()) # M이 찾으려는 비번 개수

answer = []
# site_pw_list = []
site_pw_dict = {}

for _ in range(N):
    site, pw = input().split()
    site_pw_dict[site] = pw

for _ in range(M):
    find = input()
    answer.append(site_pw_dict[find])

print('\n'.join(answer))