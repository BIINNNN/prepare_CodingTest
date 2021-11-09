def solution(record):
    answer = []
    userdict = {}  # 사용자 DB / uid가 key값, username이 value

    for sentence in record:
        sentence = sentence.split(" ")  # 공백으로 action, uid, username 구분
        if len(sentence) == 3:  # 필요한 3가지 요소 다 구분했을 때
            action, uid, username = sentence  # 해당하는 각 변수에 값 넣어줌
            userdict[uid] = username  # uid와 그에 해당하는 사용자 이름 넣어줌, 이름이 변경되면 해당 uid에 값 갱신

    for sentence in record:
        sentence = sentence.split(" ")
        #action이 Change인 경우는 아무런 메시지 출력 없음(값 갱신만 하면 됨)
        if sentence[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(userdict[sentence[1]]))
        elif sentence[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(userdict[sentence[1]]))

    return answer