import sys
sys.stdin = open("input_4861.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    result = []
    letter_table = []
    for i in range(0, N):
        letter_table.append(input()) #글자판 내용 입력

    #가로 탐색
    for r in range(N):
        for c in range(N-M+1): #하나의 행에서 반복할 수 있는 횟수 (N-M+1 ex. N=10, M=10 -> 1번(10-10+1) . N=20, M=14 -> 8번 (20-13+1))
            if letter_table[r][c:c+M] == letter_table[r][c:c+M][::-1]: #[::-1] : 역으로
                result.append(letter_table[r][c:c+M])

    #세로 탐색
    for r in range(N-M+1):
        for c in range(N):
            col_list = []
            for j in range(M):
                col_list.append(letter_table[r+j][c])
            if col_list == col_list[::-1]:
                result.append(''.join(col_list))

    print('#{} {}'.format(test_case, result[0]))