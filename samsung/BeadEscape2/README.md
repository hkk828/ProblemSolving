## 구슬 탈출 2
[문제 링크] https://www.acmicpc.net/problem/13460  

빨간 구슬, 파란 구슬, 보드의 상태가 주어졌을 때, 최소한 몇 번 기울이기를 해야 빨간 구슬만 구멍으로 빼낼 수 있는 지 구하는 문제입니다.  
주의해야할 점은 빨간 구슬만 빠지면 성공이고, 한 번의 기울이기를 통해 두 개의 구슬이 모두 빠져나가게 되는 경우도 실패입니다. 그리고 빨간 구슬을 구멍으로 빼낼 수 없거나 10번 이내에 불가능하면 -1을 출력해야 합니다.  

### 풀이
가능한 기울이기가 4가지 (위, 아래, 왼쪽, 오른쪽) 이고, 최대 10번까지만 허용하기 때문에, DFS 방식으로 총 4의 10제곱 (= 1048576) 만큼의 경우의 수를 모두 확인해보면 됩니다.  
한 번의 기울이기는 O(max(N, M)) 의 연산이 요구되므로, 전체적으로 O(1048576 * 10 * max(N, M)) 만큼의 연산이 필요합니다.  

그러나 기울이기에 대해 생각해보면 가짓 수를 많이 줄일 수 있습니다. 첫 기울이기의 경우 4가지 방향이 모두 가능하지만, 첫 기울이기가 아닌 경우에는 이전에 기울인 방향과 그 반대 방향으로는 기울여봤자 최소 움직을 구할 수 없다는 것을 알 수 있습니다.  

예를 들어 직전에 오른쪽으로 기울였다고 가정해 봅시다. 그렇다면 이미 오른쪽으로 움직일 수 있는 최대치를 움직였기 때문에, 또 오른쪽으로 기울이는 것은 의미가 없습니다.  
또한 왼쪽으로 기울이는 것도, 직전 상황에서 왼쪽으로 기울이는 것이 더 최적의 움직임이기 때문에 기울일 필요가 없음을 알 수 있습니다.  
확인해야 하는 경우의 수는 총 4*2^9 (= 2048) 가지로 감소합니다.

### 소스 코드 일부
우리가 원하는 결과를 반환하는 함수 (```num2escape```) 는 다음과 같이 정의할 수 있습니다.

```python
# 숫자에 따라 함수를 연결해주는 딕셔너리 (아래의 last_move와 동일하게 반시계 방향으로 숫자를 매겼다)
num2tilt = {
    0: tilt_up,
    1: tilt_left,
    2: tilt_down,
    3: tilt_right
}
# board의 현재 상태, 현재까지 기울인 횟수 (num_tilt), 이전 움직임 (last_move) 가 주어졌을 때, 빨간 구슬을 탈출시킬 수 있는 최소의 기울이기 횟수를 반환하는 함수
# 문제의 조건을 만족하며 빨간색 구슬을 빼낼 수 없을 때는 -1을 반환한다
def num2escape(board, num_tilt=0, last_move=None): # last_move: 0: 위, 1: 왼쪽, 2: 아래, 3: 오른쪽
    if num_tilt > 10:
        return -1
    # 파란 구슬은 남아있고, 빨간 구슬만 빠진 경우 지금까지 기울인 횟수를 반환한다
    if bead_inside(board, 'B') and not bead_inside(board, 'R'):
        return num_tilt
    # 파란 구슬인 빠진 경우, 문제의 조건을 만족하지 못하므로 -1을 반환한다
    elif not bead_inside(board, 'B'):
        return -1
    # 두 구슬 모두 남아있는 경우 DFS 방식으로 계속해서 기울이기를 이어나간다
    # 첫 기울이기의 경우 (last_move == None)
    if last_move == None:
        up = num2escape(tilt_up(board), num_tilt+1, 0)
        left = num2escape(tilt_left(board), num_tilt+1, 1)
        down = num2escape(tilt_down(board), num_tilt+1, 2)
        right = num2escape(tilt_right(board), num_tilt+1, 3)
        candidates = [up, left, down, right]
    # 첫 기울이기가 아닌 경우, 이전 기울이기 방향과 그 반대 방향은 제외한다
    else:
        # last_move, (last_move+2)%4 제외
        new_move = (last_move+1)%4
        new_move_opposite = (new_move+2)%4
        new_move_result = num2escape(num2tilt[new_move](board), num_tilt+1, new_move)
        new_move_opposite_result = num2escape(num2tilt[new_move_opposite](board), num_tilt+1, new_move_opposite)
        candidates = [new_move_result, new_move_opposite_result]
    
    # 최소 기울이기 횟수를 저장할 변수
    min_tilt = float('inf')
    for candidate in candidates:
        # 유효한 기울이기 횟수 중에서 지금까지의 최솟값보다 작으면 갱신해준다
        if 0 < candidate < min_tilt:
            min_tilt = candidate
    # 갱신이 한 번도 일어나지 않았다면 -1을, 일어났다면 그 값을 반환해준다
    return -1 if min_tilt == float('inf') else min_tilt
```

위의 함수가 작동하기 위해 주어진 board를 왼쪽으로 기울이기 하는 함수 (```tilt_left```) 를 다음과 같이 정의할 수 있고,
```python
# 왼쪽으로 기울이기를 한 board를 반환하는 함수
def tilt_left(board):
    tilted_board = []
    for idx, row in enumerate(board):
        # 첫 행과 마지막 행은 모두 막혀있다
        if idx == 0 or idx == len(board)-1:
            tilted_board.append(['#'] * len(board[0]))
            continue
        # 혅재 행에 빨간구슬, 파란구슬 모두 없으면 현재 행을 복사한다
        if 'R' not in row and 'B' not in row:
            tilted_board.append(row.copy())
            continue
        # 현재 행에 빨간구슬 혹은 파란구슬이 하나라도 있으면, 현재행에 대해서 왼쪽으로 기울이기를 해준다슬이 
        tilted_board.append(tilt_row_left(row))
    return tilted_board
```

최종적으로 하나의 행에 대해서 왼쪽으로 기울인 결과를 반환하는 함수 (```tilt_row_left```) 를 정의하여 우리가 원하는 함수 (```num2escape```) 가 잘 작동하도록 합니다.
```python
# 주어진 행을 왼쪽으로 기울이기 한 결과를 반환하는 함수
def tilt_row_left(row):
    tilted_row = row[:]

    # 빨간구슬과 파란구슬의 index를 저장한다 (없으면 -1)
    red = tilted_row.index('R') if 'R' in tilted_row else -1
    blue = tilted_row.index('B') if 'B' in tilted_row else -1

    # front에는 더 왼쪽에 있는 구슬의 index, back에는 나머지 구슬의 index를 저장한다
    front = red if red < blue else blue
    back = blue if red < blue else red

    # 최대 (행의 길이 - 3) 번까지 구슬들을 왼쪽으로 움직여준다
    for _ in range(len(row)-3):
        # 앞에 있는 구슬이 왼쪽으로 움직일 수 있는 가능성이 있는 경우만
        if front in range(2, len(row)-1):
            # 앞구슬 왼쪽에 구멍이 있으면 앞구슬을 뺀다
            if tilted_row[front-1] == 'O':
                tilted_row[front] = '.'
                front = -1
            # 앞구슬 왼쪽이 비어있으면 앞구슬을 왼쪽으로 한칸 전진시킨다
            elif tilted_row[front-1] == '.':
                tilted_row[front-1], tilted_row[front] = tilted_row[front], tilted_row[front-1]
                front -= 1

        # 뒤에 있는 구슬이 왼쪽으로 움직일 수 있는 가능성이 있는 경우만
        if back in range(2, len(row)-1):
            # 뒷구슬 왼쪽에 구멍이 있으면 뒷구슬을 뺸다
            if tilted_row[back-1] == 'O':
                tilted_row[back] = '.'
                back = -1
            # 뒷구슬 왼쪽이 비어있으면 뒷구슬을 왼쪽으로 한칸 전진시킨다
            elif tilted_row[back-1] == '.':
                tilted_row[back-1], tilted_row[back] = tilted_row[back], tilted_row[back-1]
                back -= 1

    return tilted_row
```

오른쪽으로 기울이는 함수도 비슷하게 정의할 수 있습니다. 실제 소스 코드가 제대로 작동하는 지 테스트 케이스를 통해 확인해 줍니다.
```python
from bead_escape2 import num2escape

def check(idx, my_answer, answer):
    if my_answer == answer:
        print(f'Passed test case {idx}!')
    else:
        print(f'Failed test case {idx}!')

for i in range(1, 8):
    with open(f'ex{i}.txt', 'r') as file:
        file = file.read().splitlines()
        answer = int(file[0])
        rows = file[2:]
        
    board = [list(row) for row in rows]
    check(i, num2escape(board), answer)
```

테스트 케이스에는 첫 줄에 정답, 둘째줄에 board의 사이즈, 그리고 그 다음줄부터는 board의 상태가 저장되어 있습니다.
```
1
5 5
#####
#..B#
#.#.#
#RO.#
#####
```
