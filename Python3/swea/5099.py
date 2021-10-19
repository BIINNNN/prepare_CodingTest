from collections import deque
import sys
sys.stdin = open("sample/input_5099.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    pizza = deque(enumerate(list(map(int, input().split())), start=1))
    oven = deque()

    #오븐에 넣을 수 있는 최대한의 피자를 넣어줌
    for _ in range(N):
        oven.append(pizza.popleft())

    while len(oven) != 1: #오븐에 피자가 마지막 하나가 남을때까지 반복
        if len(oven) < N and pizza: #오븐안에 빈 공간이 있고, 피자가 남은 경우
            oven.append(pizza.popleft()) #오븐의 빈 공간에 해당하는 자리에 인덱스 빠른 피자를 넣어줌

        index, cheese = oven.popleft() #오븐안에 있는 피자의 인덱스와 치즈양 확인(큐에서 뺌)

        if cheese//2 == 0: #한바퀴를 돌았을 때, 남은 치즈의 양이 0이라면
            continue #오븐에서 뺀 상태 그대로 유지하고 다음 단계 진행
        else: # 치즈가 계속 남아 있다면
            oven.append((index, cheese//2)) #반 남은 치즈양과 피자의 인덱스를 다시 집어넣음

    result = oven.popleft()[0] #마지막 남은 피자의 인덱스가 결과가 됨

    print("#{} {}".format(test_case, result))


