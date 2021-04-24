def buy_jewels(gems):
    N = len(set(gems))          # 서로 다른 보석 종류
    best_pair = [1, len(gems)]  # 모든 보석 종류를 포함하는 시작 인덱스와 끝 인덱스 리스트
    length = len(gems)          # 진열된 보석 갯수
    
    start, end = 0, 0           # 연속으로 살 때, 시작과 끝 인덱스 설정 (0에서 시작한다)
    hash_table = {gems[0]: 1}   # gems[start:end+1]의 {보석: 빈도수} 딕셔너리
    while end < len(gems):      # 진열대 끝까지 돌면서
        gem_count = len(hash_table)             # gems[start:end+1]의 서로 다른 보석 종류 갯수
        if gem_count == N:                      # 모든 종류의 보석을 가지고 있으면
            if end-start+1 < length:            # 현재 길이가 지금까지 찾은 길이보다 짧으면 업데이트
                length = end-start+1
                best_pair = [start+1, end+1]
            
            start_freq = hash_table[gems[start]]    # gems[start]는 현재 몇개가 나오는 지 확인하고
            if start_freq == 1:                     # 1개 밖에 없으면 딕셔너리에서 제거
                hash_table.pop(gems[start])
            else:                                   # 2개 이상이면 갯수를 1 빼준다
                hash_table[gems[start]] -= 1
            start +=1                               # start를 오른쪽으로 1칸 전진

        else:                                       # 아직 보석 종류가 부족하면
            end += 1                                # end를 오른쪽으로 1칸 옮겨준다
            if end == len(gems):                    # 진열대를 넘어가면 루프를 나온다
                break
            hash_table.setdefault(gems[end], 0)     # gems[end]를 딕셔너리에 넣어준다
            hash_table[gems[end]] += 1
    return best_pair


if __name__ == '__main__':
    from gems import gems1, gems2, gems3, gems4
    for gems in [gems1, gems2, gems3, gems4]:
        if buy_jewels(gems.gems) == gems.result:
            print("Passed a test case!")
        else:
            print("Failed a test case!")

