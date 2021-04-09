## 아이디 추천
[문제 링크]
https://programmers.co.kr/learn/courses/30/lessons/72410  

문자열이 주어졌을 때, 규칙에 맞는 새로운 문자열을 반환하는 문제입니다.  
특별한 아이디어가 필요하지 않고, 문제에 적힌 순서를 그대로 따라가면 어렵지 않게 해결할 수 있습니다.  

### 풀이
1단계: 먼저 ```new_id```를 소문자로 치환해 줍니다.
```python
new_id = new_id.lower()
```  

2단계, 3단계, 4단계를 각각 따로 처리해 줄 수도 있지만, 효율을 높이기 위해 한 번에 처리해 줍니다.
```python
# 알파벳 소문자, 숫자, -, _, . 인 경우만 removed_id 에 저장
removed_id = []
for char in new_id:
	# 마침표(.)가 맨처음이나 연속해서 나오면 생략
	if char == '.' and (not removed_id or removed_id[-1] == '.'):
		continue
	# 규칙에 맞는 문자인 경우 removed_id 에 추가
	if char.isalnum() or char in ['-', '_', '.']:
		removed_id.append(char)

# 만약 removed_id 가 비어있지 않고, 마지막에 . 이 있다면 제거해줍니다.
if removed_id and removed_id[-1] == '.':
	removed_id.pop()
```

5단계: 빈 문자열이 남았으면 "a"를 추가해 줍니다.  
6단계: 문자열이 16자 이상이면 첫 15자만 남기고, 끝에 오는 . 을 제거해줍니다.
```python
removed_id = ['a'] if not removed_id else removed_id[:15]
while removed_id[-1] == '.':
	removed_id.pop()
```

7단계: 문자열이 2자리 이하면, 마지막 문자를 길이가 3이 될 때까지 추가해줍니다.
```python
if len(removed_id) <= 2:
	removed_if += removed_id[-1:] * (3 - len(removed_id))
```

마지막으로 ```removed_id``` 리스트에 있는 문자들을 ```join```을 이용하여 하나의 문자열로 합쳐주고 반환해줍니다.  
```join```을 사용하지 않고 ```str``` 타입의 변수를 선언한 뒤 더해주는 식으로 하면 매번 더해줄 때마다 새로운 ```str``` 타입 변수를 생성하게 되어 비효율적입니다.  
```python
new_id = ''.join(removed_id)
return new_id
```  

### 정규 표현식(Regular expression)을 활용한 풀이
문제가 문자열을 다루고 있고, 원하는 형식이 정해져 있는 경우 정규 표현식을 활용하여 문제를 해결할 수도 있습니다.  
```python```에서는 ```re```라는 라이브러리를 이용하여 정규 표현식을 처리 할 수 있습니다.  
이 경우 코드를 간결하게 할 수 있으나 처리 속도는 느려질 수 있습니다.  

```python
import re

def solution(new_id):
    # 1단계: 소문자로 변환
    new_id = new_id.lower()

    # 2단계: 알파벳 소문자, 숫자, -, _, . 만 허용
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)

    # 3단계: 연속된 . 는 하나의 . 로 치환
    new_id = re.sub('\.+', '.', new_id)

    # 4단계: 처음이나 끝에 있는 . 제거
    new_id = new_id.strip('.')

    # 5, 6단계: 빈 문자열이면 'a'를, 16자 이상이면 15자 까지만 저장하고 끝에 . 가 있으면 제거
    new_id = 'a' if not new_id else new_id[:15]
    new_id = new_id.rstrip('.')

    # 7단계: 길이가 2자 이하면, 3자가 될 때까지 마지막 문자를 추가
    if len(new_id) < 3:
        new_id += new_id[-1] * (3 - len(new_id))
    return new_id
```
