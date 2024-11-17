1. 아스키값을 이용한 풀이

```python
def solution(s):
    answer = False
    if (len(s)==4 or len(s)==6):
        answer = True
        for i in range(len(s)):
            if ord(s[i])>64:
                answer = False
                break
    return answer


# 정수 0 ~ 9 아스키값 : 48 ~ 57

# test
print(solution("a234"))
print(solution("1234"))
```

2. isdigit()을 이용한 풀이

```python
def solution(s):
    answer = False
    if (len(s)==4 or len(s)==6):
        answer = True
        for char in s:
            if not char.isdigit():
                answer = False
                break
    return answer
```