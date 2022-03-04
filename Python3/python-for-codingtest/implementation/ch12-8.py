# 외벽점검
# 아이디어 떠올리는데 실패해서 답안 봤음.... 꼭 다시 풀어보기 한 번 풀고 두 번 풀고 세 번 또 풀어보기....꼭
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n) # 원형인 모양을 일자로 피기 위해 2배 해주는 과정
    
    # 투입 친구의 최솟값을 구해야 한다.
    # 따라서 뒤에서 처음 초기화 한 answer와 비교하면서 최솟값을 찾기 위해 dist의 길이보다 +1 한 값으로 초기화    
    answer = len(dist) + 1  

    # 0부터 length-1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구들을 나열하는 가능한 모든 경우의 수를 확인
        for friends in list(permutations(dist, len(dist))):
            cnt = 1 # 투입할 친구 수
            # 투입한 친구가 점검 할 수 있는 최종 위치
            position = weak[start]+friends[cnt-1]
            # 시작점부터 모든 취약점 확인
            for idx in range(start, start+length):
                if position < weak[idx]:
                    cnt+=1 # 점검할 수 있는 위치를 취약점이 벗어나면(다 점검하지 못하면) 새로운 친구 투입
                    if cnt > len(dist): # 투입이 더이상 불가능하면
                        break
                    position = weak[idx] + friends[cnt-1]
            answer = min(answer, cnt)
    if answer > len(dist):
        return -1
    return answer