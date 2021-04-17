'''
1. 개발 언어: cpp, java, python
2. 지원 직군: backend, frontend
3. 경력 구분: junior, senior
4. 소울 푸드: chicken, pizza
+ 코딩 테스트 점수

Q. [조건]을 만족하는 사람 중 코딩테스트 점수가 X점 이상인 사람은 모두 몇 명인가?

예시)
info = 
["java backend junior pizza 150",
"python frontend senior chicken 210",
"python frontend senior chicken 150",
"cpp backend senior pizza 260",
"java backend junior chicken 80",
"python backend senior chicken 50"]

query = 
["java and backend and junior and pizza 100",
"python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250",
"- and backend and senior and - 150",
"- and - and - and chicken 100",
"- and - and - and - 150"]

result = [1,1,1,1,2,4]
'''

# 정확성은 높지만 효율성은 낮은 코드
items = ['lang', 'dev_type', 'exp', 'food', 'score']
def process_query(infos, queries):
    # db 딕셔너리에 개발언어, 직군, 경력, 소울푸드, 점수를 key로 하여 지원자 정보 저장
    db = {'lang': [], 'dev_type': [], 'exp': [], 'food': [], 'score': []}
    for info in infos:
        info = info.split()
        db['lang'].append(info[0])
        db['dev_type'].append(info[1])
        db['exp'].append(info[2])
        db['food'].append(info[3])
        db['score'].append(info[4])

    # 각 요청에 대해
    answer = []
    for query in queries:
        # 잠재적으로 선택될 지원자 집합
        candidate = {i for i in range(len(db))}
        # 요청에서 필요한 정보만 추출
        query = query.split()
        for _ in range(3):
            query.remove('and')

        # 요청의 각 정보마다 해당하지 않는 지원자 index를 candidate 집합에서 제거
        qualified = 0
        for idx, item in enumerate(query):
            # 요청의 마지막 정보는 점수로, 해당 점수보다 크거나 같은 지원자 수 기록
            if idx == len(query) - 1:
                for id in candidate:
                    if int(db[items[idx]][id]) >= int(item):
                        qualified += 1
                break
            # 요청의 정보가 '-'인 경우에는 넘어가고, '-'가 아닌 경우에는 그에 맞게 지원자를 제거
            if item != '-':
                for id in candidate.copy():
                    if db[items[idx]][id] != item:
                        candidate.remove(id)
        answer.append(qualified)
    
    return answer

if __name__ == '__main__':
    from example import infos, queries, results

    if process_query(infos, queries) == results:
        print("Passed a test case!")
    else:
        print("Failed a test case!")