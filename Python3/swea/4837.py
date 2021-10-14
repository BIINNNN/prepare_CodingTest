import sys
sys.stdin = open("input_4837.txt", "r")

T = int(input())
# A : 1~12까지의 숫자를 가진 집합
# subset_list : 모든 부분집합이 모여있는 리스트
A = [i for i in range(1, 13)]
subset_list = []

#A의 부분집합 구하기
for i in range(1<<len(A)):
    subset = [] #부분 집합
    for j in range(len(A)):
        if i&(1<<j):
            subset.append(A[j])
    subset_list.append(subset) # 리스트에 부분집합 추가

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N : 부분집합 원소의 개수
    # K : 원소의 합

    N, K = map(int, input().split())
    result = 0 # 부분집합의 합이 K가 되는 경우

    for s in subset_list: #부분집합 갯수만큼 반복하게 됨(모든 부분집합의 경우에 대해 확인)
        if len(s) == N:
            if sum(s) == K:
                result+=1

    print("#{} {}".format(test_case, result))