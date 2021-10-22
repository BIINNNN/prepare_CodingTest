def solution(clothes):
    answer = 1
    closet = {}

    for name, kind in clothes:
        if kind in closet:
            closet[kind] += 1
        else:
            closet[kind] = 1
    # 경우의 수 구하기
    for key, values in closet.items():
        answer *= (values + 1)

    return answer - 1  # 아예 안입는 경우 제외