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
