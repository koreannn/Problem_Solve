'''
i = 1,2,3, ... 에 대해 각 숫자에 맞는 문자열을 출력하는 문제
i가 3의 배수이면서 5의 배수이면 -> "FizzBuzz"
i가 3의 배수이고 5의 배수는 아니면 -> "Fizz"
i가 3의 배수는 아니지만 5의 배수이면 -> "Buzz"
i가 아무것도 아닌 숫자라면(3의 배수도 아니고 5의 배수도 아님) -> i를 그대로 출력
'''

arr = ['0']*3

for l in range(3):
    arr[l] = input()
    
    if arr[l].isdigit():
        if l==0:
            arr[0] = int(arr[0])
            arr[1] = arr[0]+1
            arr[2] = arr[0]+2
        elif l==1:
            arr[1] = int(arr[1])
            arr[0] = arr[1]-1
            arr[2] = arr[1]+1
        else:
            arr[2] = int(arr[2])
            arr[0] = arr[2]-2
            arr[1] = arr[2]-1
print(arr)
# if (arr[2]+1)%3 == 0 and (arr[2]+1)%5 == 0:
#     print("FizzBuzz")
# elif (arr[2]+1)%3 == 0 and (arr[2]+1)%5 != 0:
#     print("Fizz")
# elif (arr[2]+1)%3 != 0 and (arr[2]+1)%5 == 0:
#     print("Buzz")
# else:
#     print(f"{(arr[2]+1)}")