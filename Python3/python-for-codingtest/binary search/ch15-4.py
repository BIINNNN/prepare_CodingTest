# 가사 검색
from bisect import bisect_right, bisect_left

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

arr = [[] for _ in range(10001)] # 모든 단어를 길이마다 나누어서 저장하기 위한 리스트 (최대 100000종류)
reversed_arr = [[] for _ in range(10001)] # 모든 단어를 길이미다 나누어서 뒤집어 저장하기 위한 리스트(접두사 와일드카드 때문)

def solution(words, queries):
    answer = []
    
    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1]) # 뒤집어서 삽입
        
    # 이진탐색 위해서 정렬
    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()
        
    for q in queries: # 쿼리 하나씩 확인하면서 처리
        if q[0] != '?': # 접미사에 와일드카드가 있는 경우
            res = count_by_range(arr[len(q)], q.replace('?', "a"), q.replace('?', 'z'))
        else:
            res = count_by_range(reversed_arr[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        # 검색 된 단어의 개수 저장
        answer.append(res)
        
    return answer