s = set()
# s = {} <- 이건 빈 "딕셔너리" 를 만드는거임
m = int(input())

for i in range(m):
    command = input()
    if command == "add":
        x = int(input())
        s.append(x)
        
    elif command == "remove":
        x = int(input())
        s.remove(x)
        
    elif command == "check":
        x = int(input())
        if x in s:
            print("1")
        else:
            print("0")
            
    elif command == "toggle":
        x = int(input())
        if x in s:
            s.remove(s)
        else:
            s.append(x)
            
    elif command == "all":
        s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
        
    elif command == "empty":
        s.clear()