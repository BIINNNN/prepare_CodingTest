def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    # 길이가 단 1차이나므로 completion 길이만큼 탐색하면서 정렬된 원소들을 비교하다가 다른 값이 나오면 중간에 한 명이 비는 것 -> participant의 해당 인덱스 값이 정답
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    # 다 비교했을 때 다른 값이 안나오면 participant의 마지막 원소가 정답
    return participant[len(participant) - 1]