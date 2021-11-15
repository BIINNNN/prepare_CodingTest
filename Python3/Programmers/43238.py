def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n  # 최대 범위

    while left <= right:
        mid = (left + right) // 2  # 현재 탐색하고 있는 사건건

        total = 0

        for time in times:
            total += mid // time
            # 심사할 인원수를 넘기는 경우
            if total >= n:
                break

        if total >= n:  # n명을 심사할 수 있는 경우
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
