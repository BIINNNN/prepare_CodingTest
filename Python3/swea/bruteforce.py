p = "is"  # p : 찾을 패턴
t = "This is a book"  # t : 전체 텍스트
M = len(p)
N = len(t)


def BruteForce(p, t):

    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    next = i
    while j < M and i < N:
        if t[i] != p[j]:
            next += 1
            i = next
            j = 0
        else:
            i = i+1
            j = j+1

    if j == M:
        return "성공" # 검색 성공
    else:
        return "실패" # 검색 실패


BruteForce(p, t)