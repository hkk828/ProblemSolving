# [문제 링크] 단어 변환 : https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

# 모든 단어의 길이는 같다는 점을 기억
# 정확히 단어 차이가 1이면 True를 반환, 아니면 False를 반환
def changeable(begin, to):
    num_diff = 0
    for char_begin, char_to in zip(begin, to):
        if char_begin != char_to:
            num_diff += 1
    return True if num_diff == 1 else False

# words 집합을 이용하여 begin에서 target으로 변환하는 최소 횟수를 반환
def min_changes(begin, target, words):
    # words 집합에 target이 없으면 불가능
    if target not in words:
        return 0
    
    distance = {begin: 0}       # begin에서 해당 단어로 변환에 필요한 최소 횟수를 저장하는 딕셔너리
    queue = deque([(begin, 0)]) # 탐색할 (단어, 최소 횟수) 들을 저장하는 큐
    while queue:                # 큐에 단어가 들어있으면 반복
        current_word, current_dist = queue.popleft()
        for word in words:
            # word를 방문한 없고, current_word에서 word로 변환이 가능한 조건이면
            # word를 방문하고, 큐에 (word, word까지 최소 횟수)를 저장한다
            if word not in distance and changeable(current_word, word):
                distance[word] = current_dist + 1
                queue.append((word, current_dist + 1))
    
    # target을 방문한 적이 있으면 distance[target]을, 방문한 적 없으면 0을 반환한다
    # distance.get(target, 0)
    return distance[target] if target in distance else 0 