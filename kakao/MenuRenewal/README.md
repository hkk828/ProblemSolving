## 메뉴 리뉴얼
[문제 링크] https://programmers.co.kr/learn/courses/30/lessons/72411

### 풀이
문자열이 주어졌을 때, 일정한 크기의 모든 조합을 만들어 낼 수 있는가가 이 문제의 핵심입니다. ```python```에서는 기본 라이브러리인 ```itertools```에서 ```combinations```이란 함수를 이용하여 모든 조합을 만들어 낼 수 있습니다.  
예를 들어, ```combinations('abc', 2)```는 ```('a', 'b'), ('a', 'c'), ('b', 'c')```를 ```iterable```로 반환합니다.

이렇게 원하는 모든 조합을 만들어 낼 수 있다면, 문제를 다음과 같이 해결할 수 있습니다.
```python
from itertools import combinations

def renew_menu(orders, course):
    course_menu = {}
    # 코스 사이즈마다 course_menu를 초기화 해줍니다
    # 이후 course_menu[코스 사이즈]에는 'best'라는 key에는 [가장 많은 득표수, 해당하는 조합들] 가 저장되고,
    # 나머지는 가능한 조합이 key가 되며 받은 득표수를 value로 갖습니다
    for num in course:
        # {'best': [best_vote, best_combinations], menu_combinations: vote}
        course_menu[num] = {'best': [0, None]}
    
    for order in orders:
        sorted_order = sorted(order)    # 메뉴 조합을 알파벳순으로 만들기 위해
        for num in course:
            # 만들려는 메뉴 조합 수 (num) 보다 크거나 같은 수의 주문이 있을 때만 작업해줍니다
            if len(order) >= num:
                # 해당 주문(order)를 통해 나올 수 있는 모든 조합을 생성하고
                menu_candidates = combinations(sorted_order, num)
                # 각 조합을 돌며 가장 많이 나온 조합을 찾습니다
                for menu_candidate in menu_candidates:
                    course_menu[num].setdefault(menu_candidate, 0)
                    course_menu[num][menu_candidate] += 1
                    # 만약 현재의 조합이 더 많은 득표를 받았다면 이에 맞게 갱신해줍니다
                    if course_menu[num][menu_candidate] > course_menu[num]['best'][0]:
                        course_menu[num]['best'][0] = course_menu[num][menu_candidate]
                        course_menu[num]['best'][1] = [menu_candidate]
                    # 만약 현재의 조합이 최고 득표와 같다면 조합만 추가해 줍니다
                    elif course_menu[num][menu_candidate] == course_menu[num]['best'][0]:
                        course_menu[num]['best'][1].append(menu_candidate)
    
    renewed_menu = []
    # 각 코스 사이즈마다
    for num in course:
        # 최고의 조합에 대한 득표가 2 이상인 경우에만 renewed_menu에 추가해줍니다
        vote, best_menus = course_menu[num]['best']
        if vote > 1:
            for best_menu in best_menus:
                renewed_menu.append(''.join(best_menu))
    # 리뉴얼된 메뉴를 알파벳순으로 정렬한 후 반환해줍니다
    renewed_menu.sort()
    return renewed_menu
```

```collections```라는 라이브러리의 ```Counter``` 클래스를 이용하면 코드를 더 짧게 작성할 수도 있습니다.

```python
from itertools import combinations
from collections import Counter # 중복되는 원소를 세야할 때 유용한 클래스

def renew_menu(orders, course):
    renewed_menu =[]

    for num in course:
        num_combinations = [] # 각 코스 사이즈의 메뉴 조합을 저장하는 변수
        for order in orders:
            if len(order) >= num:
                num_combinations += combinations(sorted(order), num)
        # num_ranks는 득표 내림차순으로 (메뉴 조합, 득표수)를 갖는다
        num_ranks = Counter(num_combinations).most_common()
        for num_menu, vote in num_ranks:
            # 최고 득표이면서 1보다 큰 경우면 renewed_menu에 추가해준다
            if vote == num_ranks[0][1] and vote > 1:
                renewed_menu.append(''.join(num_menu))
            else:
                break
    # 리뉴얼된 메뉴 알파벳 순으로 정렬된 리스트 반환
    return sorted(renewed_menu)
```