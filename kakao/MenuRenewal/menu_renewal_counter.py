from itertools import combinations
from collections import Counter

def renew_menu(orders, course):
    renewed_menu =[]

    for num in course:
        num_combinations = []
        for order in orders:
            if len(order) >= num:
                num_combinations += combinations(sorted(order), num)
        num_ranks = Counter(num_combinations).most_common()
        for num_menu, vote in num_ranks:
            if vote == num_ranks[0][1] and vote > 1:
                renewed_menu.append(''.join(num_menu))
            else:
                break
    return sorted(renewed_menu)