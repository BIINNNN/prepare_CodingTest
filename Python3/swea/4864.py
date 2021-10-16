import sys
sys.stdin = open("input_4864.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = str(input())
    str2 = str(input())

    if str1 in str2:
        result = 1
    else:
        result = 0

    print("#{} {}".format(test_case, result))