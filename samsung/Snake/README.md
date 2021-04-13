## 뱀
[문제 링크] https://www.acmicpc.net/problem/3190
위의 링크에 설명된 방식으로 뱀이 움직일 때, 게임이 끝날 때 까지의 시간을 구하는 문제입니다.

### 풀이
기본적으로 보드의 크기(```board_size```), 사과의 위치(```apples```), 시간에 따른 방향 전환(```moves```)이 입력으로 주어집니다. 여기에 계속해서 뱀의 상태를 추적하기 위해 deque 자료구조를 이용하였습니다.  

뱀의 상태를 기록하는 deque의 앞부분은 뱀의 머리에 해당하고 마지막은 꼬리에 해당합니다.

```python
# 뱀은 가장 왼쪽 상단에서 길이가 1인 상태로 시작한다
snake = deque([(0, 0)])
print(release_snake(snake, N, apples, moves))
```

```release_snake```라는 함수는 뱀의 상태, 보드의 크기, 사과의 위치, 방향 전환 정보, 그리고 현재 시간을 입력으로 받아서, 게임이 끝나는 시간을 반환합니다. deque은 built-in library인 ```collections```에서 가져왔습니다.

```python
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
```

위의 함수를 아래와 같이 테스트 해볼 수 있습니다.
```python
import os
from snake import release_snake, deque
test_files = sorted(os.listdir('test_cases'))

for test_file in test_files:
    with open(f'test_cases/{test_file}', 'r') as test_case:
        data = test_case.read().splitlines()
        answer = int(data[0])
        N, K = map(int, data[1:3])
        apples = {tuple(map(lambda x: int(x)-1, apple.split())) for apple in data[3:3+K]}
        L = data[3+K]
        moves = {}
        for move in data[4+K:]:
            time, direction = move.split()
            moves[int(time)] = direction

    if release_snake(deque([(0, 0)]), N, apples, moves) == answer:
        print("Passed a test case!")
    else:
        print("Failed a test case!")
```