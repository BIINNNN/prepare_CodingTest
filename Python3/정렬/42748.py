def solution(array, commands):
    answer = []

    for command in commands:
        array_slice = array[command[0] - 1:command[1]]  # 인덱스가 i보다 1 작음
        array_slice.sort()
        answer.append(array_slice[command[2] - 1])  # 정렬한 배열의 k번째에 해당하는 값들을 answer에 저장함
    return answer