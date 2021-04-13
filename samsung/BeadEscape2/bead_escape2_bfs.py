from collections import deque

# 현재 상태를 저장할 클래스
# 빨간구슬과 파란구슬의 위치를 tuple로 저장하고, 현재까지 기울인 횟수, 마지막 기울이기의 방향을 저장한다
class Status:
    def __init__(self, red_pos = None, blue_pos = None, num_tilt = 0, last_move = None):
        self.red_pos = red_pos
        self.blue_pos = blue_pos
        self.num_tilt = num_tilt
        self.last_move = last_move

# 기울이기의 방향에 따른 단위 움직임을 딕셔너리로 정의
moves = {
    0: [-1, 0], # up
    1: [0, -1], # left
    2: [1, 0],  # down
    3: [0, 1]   # right
}
    
# BFS 아이디어를 사용한 함수
def num2escape_bfs(board, status):
    # deque으로 queue를 구현
    status_queue = deque([status])

    # queue가 비어있지 않으면 계속해서 루프를 돈다
    while status_queue:
        status = status_queue.popleft()

        # 기울이기가 10번을 넘어가면 -1 반환
        if status.num_tilt > 10:
            return -1

        # 현재 빨간구슬과, 파란구슬의 위치를 읽어온다
        current_red_row, current_red_col = status.red_pos
        current_blue_row, current_blue_col = status.blue_pos
        
        # 만약 빨간구슬이 구멍으로 빠지고, 파란구슬은 남아있으면 현재까지의 기울이기 횟수를 반환한다
        if board[current_red_row][current_red_col] == 'O' and board[current_blue_row][current_blue_col] != 'O':
            return status.num_tilt
        # 만약 파란구슬이 구멍으로 빠졌다면, 현재의 상태는 무시하고 queue의 다음 상태를 가져온다
        elif board[current_blue_row][current_blue_col] == 'O':
            continue
        
        # 두 구슬이 모두 board에 남아 있으면 네 방향으로 기울이기를 진행한다
        for move, (d_row, d_col) in moves.items():
            # 이전 기울이기의 방향과 그 반대 방향은 제외하고 탐색한다
            if status.last_move in [move, (move+2)%4]:
                continue

            # 기울였을 때의 두 구슬의 위치를 저장한 변수
            new_red_row, new_red_col = status.red_pos
            new_blue_row, new_blue_col = status.blue_pos

            # 먼저 빨간 공을 전진시킨다. 앞에 있는 칸이 막혀있거나 구멍이 아니면 전진
            while board[new_red_row + d_row][new_red_col + d_col] not in ['#', 'O']:
                new_red_row += d_row
                new_red_col += d_col

            # 만약 앞에 있는 칸이 구멍이었다면 구멍으로 넣어준다
            if board[new_red_row + d_row][new_red_col + d_col] == 'O':
                new_red_row += d_row
                new_red_col += d_col

            # 파란 공에 대해서도 위와 똑같이 해준다
            while board[new_blue_row + d_row][new_blue_col + d_col] not in ['#', 'O']:
                new_blue_row += d_row
                new_blue_col += d_col

            if board[new_blue_row + d_row][new_blue_col + d_col] == 'O':
                new_blue_row += d_row
                new_blue_col += d_col

            # 두 공이 각각 움직인 거리를 계산한다
            red_moves = abs(current_red_row - new_red_row) + abs(current_red_col - new_red_col)
            blue_moves = abs(current_blue_row - new_blue_row) + abs(current_blue_col - new_blue_col)
            # 만약 두 공이 같은 위치에 있는 경우를 처리해준다
            if (new_red_row, new_red_col) == (new_blue_row, new_blue_col):
                # 두 공이 구멍에 있으면 그대로두고,
                # 만약 구멍아니라면 더 많이 이동한 공을 한 칸 뒤로 이동시킨다
                if board[new_red_row][new_red_col] != 'O':
                    if red_moves > blue_moves:
                        new_red_row -= d_row
                        new_red_col -= d_col
                    else:
                        new_blue_row -= d_row
                        new_blue_col -= d_col

            # 만약 공의 움직임이 있었으면 큐에 현재 상태 저장하고, 없었으면 무시한다
            if red_moves or blue_moves:
                new_red_pos = (new_red_row, new_red_col)
                new_blue_pos = (new_blue_row, new_blue_col)
                status_queue.append(Status(new_red_pos, new_blue_pos, status.num_tilt+1, move))
    # 모든 상태에 대해서 불가능한 경우 -1
    return -1

if __name__ == '__main__':
    N, M = map(int, input().split())
    status = Status()
    board = []
    for row_idx in range(N):
        row = list(input())
        board.append(row)
        if 'R' in row:
            status.red_pos = (row_idx, row.index('R'))
        if 'B' in row:
            status.blue_pos = (row_idx, row.index('B'))

    print(num2escape_bfs(board, status))