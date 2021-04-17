# 정확성과 효율성 모두 높은 코드
langs = ['python', 'java', 'cpp', '-']
dev_types = ['backend', 'frontend', '-']
exps = ['junior', 'senior', '-']
foods = ['pizza', 'chicken', '-']

# lst에서 value보다 크거나 같은 원소의 개수를 반환
def greater_than_or_equal(lst, value):
    left, right = 0, len(lst)
    
    while left < right:
        mid = (left + right) // 2
        if lst[mid] >= value:
            right = mid
        else:
            left = mid + 1
    return len(lst) - right

def process_query(infos, queries):
    # (언어, 직군, 경력, 음식)을 key로 하는 딕셔너리 db 초기화 ('-'도 포함)
    db = {}
    for lang in langs:
        for dev_type in dev_types:
            for exp in exps:
                for food in foods:
                    db[(lang, dev_type, exp, food)] = []
    
    # 각 응시자의 정보가 주어지면, 그 정보에 대응하는 16가지 조합에 대해 현재 점수 저장
    # 예) ['java', 'backend', 'junior', 'pizza'] -> ('-', 'backend', '-', 'pizza'), ('java', '-', 'junior', '-'), ...
    for info in infos:
        info = info.split()
        score = int(info.pop())
        
        for lang in [info[0], '-']:
            for dev_type in [info[1], '-']:
                for exp in [info[2], '-']:
                    for food in [info[3], '-']:
                        db[(lang, dev_type, exp, food)].append(score)
    
    # db에 저장된 점수 리스트를 모두 오름차순으로 정렬
    for key in db:
        db[key].sort()

    # 각 요청에 해당하는 지원자 점수 리스트를 db에서 불러온 뒤, 요청의 점수보다 크거나 같은 지원자 수를 저장
    answer = []
    for query in queries:
        query = query.split()
        score = int(query.pop())
        query = (query[0], query[2], query[4], query[6])
        answer.append(greater_than_or_equal(db[query], score))
    return answer

if __name__ == '__main__':
    from example import infos, queries, results

    if process_query(infos, queries) == results:
        print("Passed a test case!")
    else:
        print("Failed a test case!")