import sys
from itertools import permutations

sys.stdin = open("sample/input_5189.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)] # 각 구역 이동시 배터리 사용량

    result = 1000 #100이하의 자연수가 최대 10줄 가능하므로 나올 수 있는 가장 큰 값을 임의로 할당
    i = 0
    for arr in permutations(range(1, N)): #N개의 방문지 있을 때, 만들 수 있는 경우의 수 모두 생성해서 리스트 저장
        total_battery = battery[0][arr[0]]
        for i in range(len(arr)-1): #처음으로 돌아오는 마지막 경우 제외
            total_battery += battery[arr[i]][arr[i+1]]
        total_battery += battery[arr[i+1]][0]

        if result > total_battery:
            result = total_battery

    print("#{} {}".format(test_case, result))