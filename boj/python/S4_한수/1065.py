n = int(input())
dp = [0]*(n+1) 

def check_num(num_list: list) -> bool:
    check = num_list[0] - num_list[1]
    for i in range(len(num_list)-1):
        curr = num_list[i]-num_list[i+1]
        if curr != check:
            return False
    return True

for i in range(1, n+1):
    if i < 100: # 1~99까지는 각각 1~99
        dp[i] = i
    else: # 100부터는 다름
        check = False  # 자기 자신이 한수인지 체크하는 값
        curr_num = i
        each_num = []
        
        while curr_num>0:
            each_num.append(curr_num%10)
            curr_num = curr_num//10
        
        check = check_num(each_num)
        
        dp[i] = dp[i-1] + check

print(dp[n])