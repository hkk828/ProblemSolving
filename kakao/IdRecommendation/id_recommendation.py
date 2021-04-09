def recommend_id(new_id):
    # 규칙
    # 1. 아이디 길이 3~15자
    # 2. 아이디는 알파벳 소문자, 숫자, -, _, . 만 사용 가능
    # 3. 단, . 는 처음과 끝에 사용할 수 없고, 연속으로 사용할 수 없음
    
    # 검사 프로세스
    # 1단계: 모든 대문자를 소문자로 치환
    new_id = new_id.lower()

    # 2단계: 알파벳 소문자, 숫자, -, _, . 제외한 문자 제거
    # 3단계: . 가 2번 이상 연속된 부분 하나로 치환
    # 4단계: . 가 처음이나 끝에 위치하면 제거
    removed_id = []
    for char in new_id:
        if char == '.' and (not removed_id or removed_id[-1] == '.'):
            continue
        if char.isalnum() or char in ['-', '_', '.']:
            removed_id.append(char)
    if removed_id and removed_id[-1] == '.':
        removed_id.pop()

    # 5단계: 빈 문자열이면 "a" 대입
    # 6단계: 16자 이상이면 첫 15자만 남기고, 제거한 후 . 마지막에 있으면 제거
    removed_id = ['a'] if not removed_id else removed_id[:15]
    while removed_id[-1] == '.':
        removed_id.pop()

    # 7단계: 2자리 이하면, 마지막 문자를 길이가 3이 될때까지 붙인다
    if len(removed_id) <= 2:
        removed_id += removed_id[-1:] * (3-len(removed_id))
        
    new_id = ''.join(removed_id)
    return new_id