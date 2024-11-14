1. 0의 아스키값은 48이다.

2. for루프 내에서 i값을 수동으로 증가시키려 해봤자 값은 안바뀐다.

```python
for i in range(5):
    print(f"시작: i = {i}")
    if i == 2:
        i += 2
        print(f"  i를 2 증가시킴: i = {i}")
    print(f"끝: i = {i}")
```
(이건 내가 뭘 잘못알고있나 했는데 c는 수동 증가 된다)
```cpp
#include<iostream>

int main()
{
    int i;
    for(i=0;i<5;i++)
    {
        std::cout << i << std::endl;
        i+=3;
    }
    return 0;
}
```
`range()`를 통한 for루프에서는 i를 수동으로 조절하는게 안된다.
- `for i in range(len(s))`에서 `i`의 값은 매 반복마다 `range()` 객체에 의해 자동으로 설정된다.
- 루프 내부에서 `i`의 값을 변경해도(e.g. `i += 3`), 다음 반복이 시작될 때 `range()` 객체가 다시 i의 값을 설정한다.
- 즉 파이썬이라서 안되는게 아니라 `range()`때문에 안되는거다

3. 각 분기에 continue해줄 필요 없다.
c언어의 else if도 마찬가지다 (switch문이랑 헷갈렸음)

무식하게 분기로 풀 수도 있고, 아니면 `num_dict`를 만들어서 풀 수도 있겠다.



