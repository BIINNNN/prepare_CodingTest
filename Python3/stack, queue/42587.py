from collections import deque

def solution(priorities, location):
    answer = 0
    p_list = deque([(value, index) for index, value in enumerate(priorities)])
    
    while p_list:
        now_job = p_list.popleft()
        if p_list:
            if now_job[0] < max(p_list)[0]:
                p_list.append(now_job)
            else:
                answer += 1
                if now_job[1] == location:
                    break
        else:
            answer += 1
            if now_job[1] == location:
                break
                
    return answer