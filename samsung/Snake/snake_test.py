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