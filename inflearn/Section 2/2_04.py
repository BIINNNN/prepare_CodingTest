#대표값

import sys
sys.stdin = open("D:\input.txt","rt")

n = int(input())
scores = list(map(int, input().split()))
avg = sum(scores)/n # 평균 점수
#반올림
avg += 0.5
avg = int(avg)

numMin = float('inf') #최소 점수 차이를 찾기 위해 초기엔 무한히 큰 수로 초기화

for idx, x in enumerate(scores): #idx : 학생 번호
    num = abs(x - avg) #평균값에 가까운 점수를 찾기 위해 차이에 절댓값 씌움
    if num < numMin : #차이가 가장 작은 경우
        numMin = num
        score = x
        answer = idx + 1
    elif num == numMin: #차이가 같은 학생이 있는 경우
        if x > score : #평균값 - 점수가 같은 x 값이 현재 numMin에 있는 점수보다 크다면
            score = x #점수가 높은 학생의 번호를 답으로 해야하기 때문
            answer = idx +1
            
print(avg, answer)        