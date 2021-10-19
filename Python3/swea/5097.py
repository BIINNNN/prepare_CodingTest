import sys
sys.stdin = open("sample/input_5097.txt","r")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))

    result = numbers[M%N]

    print("#{} {}".format(test_case, result))
