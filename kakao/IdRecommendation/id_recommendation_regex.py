import re

def solution(new_id):
    # 1단계: 소문자로 변환
    new_id = new_id.lower()

    # 2단계: 알파벳 소문자, 숫자, -, _, . 만 허용
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)

    # 3단계: 연속된 . 는 하나의 . 로 치환
    new_id = re.sub('\.+', '.', new_id)

    # 4단계: 처음이나 끝에 있는 . 제거
    new_id = new_id.strip('.')

    # 5, 6단계: 빈 문자열이면 'a'를, 16자 이상이면 15자 까지만 저장하고 끝에 . 가 있으면 제거
    new_id = 'a' if not new_id else new_id[:15]
    new_id = new_id.rstrip('.')
    
    # 7단계: 길이가 2자 이하면, 3자가 될 때까지 마지막 문자를 추가
    if len(new_id) < 3:
        new_id += new_id[-1] * (3 - len(new_id))
    return new_id