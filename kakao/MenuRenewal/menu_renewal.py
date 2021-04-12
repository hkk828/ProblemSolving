from itertools import combinations

def renew_menu(orders, course):
    course_menu = {}
    for num in course:
        course_menu[num] = {'best': [0, None]}   # {'best': [best_vote, best_combinations], menu_combinations: vote}
    
    for order in orders:
        sorted_order = sorted(order)
        for num in course:
            if len(order) >= num:
                menu_candidates = combinations(sorted_order, num)
                for menu_candidate in menu_candidates:
                    course_menu[num].setdefault(menu_candidate, 0)
                    course_menu[num][menu_candidate] += 1
                    if course_menu[num][menu_candidate] > course_menu[num]['best'][0]:
                        course_menu[num]['best'][0] = course_menu[num][menu_candidate]
                        course_menu[num]['best'][1] = [menu_candidate]
                    elif course_menu[num][menu_candidate] == course_menu[num]['best'][0]:
                        course_menu[num]['best'][1].append(menu_candidate)
    
    renewed_menu = []
    for num in course:
        vote, best_menus = course_menu[num]['best']
        if vote > 1:
            for best_menu in best_menus:
                renewed_menu.append(''.join(best_menu))
    renewed_menu.sort()
    return renewed_menu


