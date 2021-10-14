import sys
sys.stdin = open("input_4839.txt", "r")

T = int(input())

def binarySearch(page, target):
    l = 1
    r = page
    count = 0

    while (r - l > 1):  # 남은 장수가 두 장 이하이면 탈출
        c = (l + r) // 2
        count+=1 #n번째 시도

        if target == c:
            break
        elif target > c:
            l = c
        else: #target < c
            r = c

    if l+1 == r: #두 장 남았을 경우
        count+=1

    return count
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    count_a = binarySearch(P, Pa)
    count_b = binarySearch(P, Pb)

    result = 0
    if count_a > count_b:
        result = 'B'
    elif count_a < count_b:
        result = 'A'

    print("#{} {}".format(test_case, result))








