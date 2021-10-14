import sys
sys.stdin = open("input_4836.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input()) #칠할 영역의 수
    area = [[0 for _ in range(10)] for _ in range(10)] #전체 영역 (0: 흰, 1: 빨, 2: 파. 3: 보)
    count=0 #해당 영역에 3인 경우 카운트 저장할 변수

    for i in range(0, N):
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if color==1:
                    if area[r][c]==0:
                        area[r][c]=1
                    elif area[r][c]==2:
                        area[r][c]=3
                        count+=1
                if color==2:
                    if area[r][c]==0:
                        area[r][c]=2
                    elif area[r][c]==1:
                        area[r][c]=3
                        count+=1
    print("#{} {}".format(test_case, count))


