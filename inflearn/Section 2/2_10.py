#점수계산

import sys
sys.stdin = open("D:\input.txt","rt")

n = int(input())
sols = list(map(int, input().split()))
score = 0
cnt = 0

for sol in sols:
    if sol == 1:
        # 1이 나온 횟수만큼 가중치 더해짐(ex. 첫 번째 1 - 1점 , 연속한 두 번째 1 등장 - 2점..)
        # 따라서 1이 나올때마다 가중치 1씩 더해줌
        cnt+=1
        score+=cnt
    else:
        #맞추지 못했을 때는 어차피 더해지는 점수는 없으므로 연속된 경우 높아진 가중치만 다시 초기화 해주면 됨.
        cnt = 0
    
print(score)