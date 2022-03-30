# 실패율
def solution(N, stages):
    answer = {} # 실패율 저장 {stage_idx : 실패율}
    challenger = len(stages)
    
    for stage in range(1, N+1):
        if challenger != 0:
            count = stages.count(stage)
            answer[stage] = count/challenger
            challenger -= count
        else: # 도달한 유저가 없는 경우
            answer[stage] = 0
            
    
    return sorted(answer, key = lambda x : answer[x], reverse=True)