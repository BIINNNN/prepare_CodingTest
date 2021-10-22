def solution(citations):
    answer = 0
    l = len(citations)
    citations.sort()
    #오름차순 정렬되었으므로 해당 인덱스 이후의 원소들은 모두 h번 이상 인용된 논문들로 이루어져 있음
    for i in range(l):
        if citations[i] >= l-i: #논문이 인용된 횟수 >= 인용된 논문의 개수
            return l-i
    return answer