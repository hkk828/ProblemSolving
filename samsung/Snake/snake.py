from collections import deque

# coord가 n x n 보드 안에 있는 지 확인하는 함수
def in_board(n, coord):
    return 0<=coord[0]<n and 0<=coord[1]<n

# 뱀 게임을 시작하여, 끝나는 시간을 반환한다
def release_snake(snake, board_size, apples, moves, current_time=0):
    unit_moves = {
        0: [-1, 0], # 위
        1: [0, -1], # 왼쪽
        2: [1, 0],  # 아래
        3: [0, 1]   # 오른쪽
    }
    facing = 3  # right
    hit = False # 뱀이 자기 몸이나 벽에 부딪혔는 지 체크하는 변수
    # 부딪치지 않았으면 게임을 이어서한다
    while not hit:
        # 현재 시간에 맞춰 방향을 전환해야 하는지 확인한다
        turn = moves[current_time] if current_time in moves else None
        # 방향을 전환하는 경우 뱀이 바라보는 방향 (facing) 을 바꿔준다
        if turn != None:
            if turn == 'L':
                facing = (facing+1)%4
            elif turn == 'D':
                facing = (facing-1)%4
        d_move = unit_moves[facing] # 바라보는 방향으로 한 칸 이동하는 움직임
        head = snake[0]             # 현재 뱀의 머리 위치
        front = (head[0]+d_move[0], head[1]+d_move[1])  # 뱀 머리 앞의 위치

        # 뱀 머리 앞이 몸에 부딪히거나 벽에 부딪힌 경우
        if front in snake or not in_board(board_size, front):
            hit = True
        # 몸에 부딪히지 않고, 벽에도 부딪히지 않았을 때
        else:
            if front in apples:         # 앞에 사과가 있으면 꼬리를 땡기지 않는다
                apples.remove(front)    # 먹은 사과 제거
                snake.appendleft(front) # 길이 1증가
            else:
                snake.appendleft(front) # 머리 내밀고
                snake.pop()             # 꼬리 땡기고

        current_time += 1               # 1초 경과
    return current_time

if __name__ == '__main__':
    N = int(input())
    K = int(input())
    shift_idx = lambda x:  int(x)-1     # 1행 1열 부터 시작하므로 index로 사용하기 위해 1씩 빼준다
    apples = {tuple(map(shift_idx, input().split())) for _ in range(K)}
    L = int(input())
    moves = {}
    for _ in range(L):
        time, direc = input().split()
        moves[int(time)] = direc

    # 뱀은 가장 왼쪽 상단에서 길이가 1인 상태로 시작한다
    snake = deque([(0, 0)])
    print(release_snake(snake, N, apples, moves))