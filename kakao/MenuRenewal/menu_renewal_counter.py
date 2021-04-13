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