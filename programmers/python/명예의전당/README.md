k=3 -->

- 3일 이후부터는 해당 날짜에서 나온 점수가 기존 명예의 전당 점수들보다 클 경우 전당에 올라가고,
기존에 있던 3번째 사람이 내려감
- 3일까지는 해당 날짜에서 나온 사람 모두 오름차순으로 들어가기만 하면 됨.
- 발표 점수란, k=3짜리 배열(?) 에서 가장 낮은 점수를 의미

- score와 k값을 통해 발표점수를 반환해내야 함


이런거 안됨 (sort()는 원본을 바꿈)
```python
l = [10, 20, 30, 40, 50]
k = 3

rank = l[:k].sort(reverse=True) # None : sort() 별도 반환값 없이 원본을 바꾸고, 반환값은 None이므로 의도랑 다르게 작동
rank = sorted(l[:k], reverse=True) # 이게 맞음
print(rank)
```

> Q. sorted()로 정렬시키고 맨 뒤의 인덱스에 접근하는게 효율적일까, min으로 최소값을 찾아내는게 효율적일까

sorted()로 작성한 방식은 아래와 같았다.

```python
def solution(k, score):
    answer = []
    ranking = []

    for i in score:
        ranking.append(i)
        ranking = sorted(ranking, reverse=True)[:k] # 상위 k개에 대해서만 정렬 유지
        answer.append(ranking[-1])

    return answer
```
(기존 코드)
```python
def solution(k, score):
    answer = []
    ranking = []
    
    for i in range(len(score)):
        if i < k:
            ranking.append(score[i])
        else:
            if min(ranking) < score[i]:
                ranking.remove(min(ranking))
                ranking.append(score[i])
        answer.append(min(ranking))
    return answer
```

기존 코드보다 깔끔한것도 그렇고, 성능을 봤을 때도 sorted()를 이용한 방법이 더 좋다고 판단했다.

다만 시간 복잡도만 보면,
- min 기반 : O(3*n*k) = O(n*k)
- sorted 기반 : O(k*logk)

min기반의 방식이 더 효과적으로 보이지만 k값이 커지면 sorted방식이 효과적일 것이다.