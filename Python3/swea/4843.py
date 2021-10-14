import sys
sys.stdin=open("input_4843.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # 정수의 개수
    ai = list(map(int, input().split()))
    result = []
    #10개까지 출력
    for i in range(0, 10):
        max_num, min_num = ai[0], ai[0]

        index = 0
        # 가장 큰 수부터 시작해서 큰 수, 작은 수 가 번갈아가며 저장되어야 함.
        # 인덱스 0부터 시작하면 0, 2, .. ,8 까지 짝수번 인덱스에는 큰 수가 들어갈 차례고,
        # 1, 3, .. , 9의 홀수번 인덱스에는 작은 수가 들어갈 차례이다.
        if i % 2 == 0: #최댓값이 있는 인덱스 탐색
            for j in range(len(ai)):
                if ai[j] >= max_num:
                    max_num = ai[j]
                    index = j
        else: #최솟값이 있는 인덱스 탐색
            for j in range(len(ai)):
                if ai[j] <= min_num:
                    min_num = ai[j]
                    index = j

        result.append(ai.pop(index)) #최댓값 혹은 최솟값의 인덱스를 결과를 출력할 리스트에 저장하고, 기존 리스트에서 삭제

    result = ' '.join(map(str, result))
    print("#{} {}".format(test_case, result))





