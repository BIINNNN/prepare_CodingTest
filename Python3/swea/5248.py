import sys
sys.stdin = open("sample/input_5248.txt", "r")

T = int(input())

#x를 포함하는 집합을 찾는 연산
def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

def union(x, y):
    parent[find_set(y)] = find_set(x)

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    votes = list(map(int, input().split()))
    #출석번호의 인덱스까지 부모리스트 만들고, 초기엔 부모를 자기 자신으로 정의
    parent = [i for i in range(N+1)]

    for i in range(0, M*2, 2): #두 개씩 잘라서 한 쌍마다 union
        union(votes[i], votes[i+1])

    result = set()

    for i in range(1, N+1):
        result.add(find_set(i))

    print("#{} {}".format(test_case, len(result)))
