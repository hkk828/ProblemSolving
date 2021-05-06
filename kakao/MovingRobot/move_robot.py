# 문제링크: https://programmers.co.kr/learn/courses/30/lessons/60063#
from collections import deque

def get_possible_moves(first, second, ext_board):
    candidates = []
    
    delta = [
        [-1, 0], # up
        [0, 1],  # right
        [1, 0],  # down
        [0, -1]  # left
    ]
    for direction in delta:     # translation
        drow, dcol = direction
        new_first = (first[0]+drow, first[1]+dcol)
        new_second = (second[0]+drow, second[1]+dcol)
        if ext_board[new_first[0]][new_first[1]] == 0 and ext_board[new_second[0]][new_second[1]] == 0:
            candidates.append((new_first, new_second))

    if first[0] == second[0]:   # rotation (when horizontal)
        for d in [-1, 1]:
            if ext_board[first[0]+d][first[1]] == 0 and ext_board[second[0]+d][second[1]] == 0:
                candidates.append((first, (first[0]+d, first[1])))
                candidates.append((second, (second[0]+d, second[1])))

    else:                       # rotation (when vertical)
        for d in [-1, 1]:
            if ext_board[first[0]][first[1]+d] == 0 and ext_board[second[0]][second[1]+d] == 0:
                candidates.append(((first[0], first[1]+d), first))
                candidates.append(((second[0], second[1]+d), second))

    return candidates

def get_min_time(board):
    N = len(board)
    new_board = [[1] * (N+2) for _ in range(N+2)]  # outer walls
    for rowIdx, row in enumerate(board):
        new_board[rowIdx+1][1:N+1] = row
    
    queue = deque([((1, 1), (1, 2), 0)])
    visited = set([((1, 1), (1, 2))])
    
    while queue:
        first, second, time = queue.popleft()

        if first == (N, N) or second == (N, N):
            return time

        for next_move in get_possible_moves(first, second, new_board):
            if next_move not in visited and (next_move[1], next_move[0]) not in visited:
                queue.append((*next_move, time+1))
                visited.add(next_move)
    raise Exception("This does not have an answer!")

board = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]
]
print(get_min_time(board))