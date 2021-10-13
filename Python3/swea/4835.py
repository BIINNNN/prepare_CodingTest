import sys
sys.stdin = open("input_4835.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    max_sum = 0
    min_sum = 0

    for i in range(0, M):
        min_sum += ai[i]

    for i in range(0, N-M+1):
        temp = 0
        for j in range(0, M):
            temp += ai[i+j]

        if temp > max_sum:
            max_sum = temp
        if temp < min_sum:
            min_sum = temp

    print("#{} {}".format(test_case, (max_sum-min_sum)))


