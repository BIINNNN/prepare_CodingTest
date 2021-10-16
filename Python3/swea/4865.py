import sys
sys.stdin = open("input_4865.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = {}

    for i in str1:
        result[i] = str2.count(i)

    print('#{} {}'.format(test_case, max(result.values())))
