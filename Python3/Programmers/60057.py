def solution(s):
    answer = 1000  # 최악의 경우는 1000자리의 s에서 반복되는 구간이 하나도 나오지 않을 때

    # 슬라이싱해서 반복이 나올 수 있는 경우의 최대 길이 = 문자열 길이의 절반(최소 2번 하나의 동일 문자열 반복 가능)
    if len(s) == 1:
        return 1

    for i in range(1, len(s) // 2 + 1):
        result = ''
        count = 1
        tmp = s[:i]  # 반복마다 단위 문자열 초기화 해줘야 함

        for j in range(i, len(s) + i, i):
            # 현재 문자열 슬라이싱과 다음 문자열이 같다면
            if tmp == s[j:j + i]:
                count += 1

            # 같지 않다면 새로운 단위 문자열이므로 count가 1이됨을 고려해줘야 함
            else:
                # 반복 개수가 2개 이상이면 반복 횟수와 반복되는 문자열이 함께 나와야 함
                if count != 1:
                    result = result + str(count) + tmp
                    # 반복 개수가 1개면 1은 제외하고 문자열만 나옴
                elif count == 1:
                    result += tmp

                tmp = s[j:j + i]  # 현재 슬라이싱 이후 문자열을 현재 슬라이싱 문자열로
                count = 1

        answer = min(answer, len(result))
    return answer