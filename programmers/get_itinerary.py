# [문제 링크] 여행경로: https://programmers.co.kr/learn/courses/30/lessons/43164#

# 재귀함수를 사용한 풀이 (recursive solution)
# "starting_city"에서 시작하여 모든 항공권을 사용하는 경로를 반환하는 함수
def get_itinerary(num_tickets, ticket_box, start_city = "ICN"):
    path = [start_city]
    if start_city not in ticket_box:    # 현재 도시에서 출발하는 항공권이 없는 경우 [start_city] 반환
        return path
    
    for next_city in sorted(ticket_box[start_city]):                       # 현재 도시에서 출발하는 항공권이 있는 경우, 사용하지 않은 항공권을 알파벳 순으로 확인
        ticket_box[start_city].remove(next_city)                           # 다음 도시로 가는 항공권 사용
        rest_path = get_travel_path(num_tickets-1, ticket_box, next_city)  # 다음 도시부터 출발해서 (지금 까지의 경로를 제외한) 모든 항공권을 사용하는 경로 탐색
        if len(rest_path) == num_tickets:                                  # 찾은 경로가 모든 티켓을 사용했으면, 현재 도시에 덧붙여 반환
            return path + rest_path                                        
        ticket_box[start_city].append(next_city)                           # 찾은 경로가 모든 티켓을 사용하지 못했으면, 다음 도시로 가는 항공권 쓰지 않고, 다른 도시 탐색
    return path                                                            # 만약 현재도시에서 출발하는 티켓을 모두 사용한 경우 현재까지의 path 반환

def solution(tickets):
    ticket_box = {}                                 # tickets 리스트를 {출발도시: [도착도시들]} 형식의 딕셔너리로 변환
    for start, end in tickets:
        ticket_box.setdefault(start, [])
        ticket_box[start].append(end)
    return get_itinerary(len(tickets), ticket_box)


# 반복문을 사용한 풀이 (iterative solution)
# def get_itinerary(tickets):
#     ticket_box = {}                               # 위와 같이 tickets 리스트를 딕셔너리로 변환
#     for start, end in tickets:
#         ticket_box.setdefault(start, [])
#         ticket_box[start].append(end)
    
#     for _, destinations in ticket_box.items():    # 딕셔너리에서 도착지 리스트를 알파벳 역순으로 정렬
#         destinations.sort(reverse=True)
        
#     final_path = []                               # 최종 여행 경로가 역순으로 저장될 리스트
#     options = ["ICN"]                             # 다음 선택지를 저장하는 스택
#     while options:                                # options 스택에 다음 선택지가 있으면 반복
#         current_city = options[-1]                # options 스택 가장 윗 도시를 불러와서
                                                    # 더 이상 이동할 수 없으면, final_path에 경로로 추가해준다
#         if current_city not in ticket_box or len(ticket_box[current_city]) == 0:  
#             final_path.append(options.pop())
#         else:                                     # 계속 이동할 수 있으면, 알파벳 순서로 가장 빠른 다음 도시를 스택에 추가해준다
#             options.append(ticket_box[current_city].pop())
#     return final_path[::-1]                       # final_path를 뒤집어서 반환한다