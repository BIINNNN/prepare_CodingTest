def solution(progresses, speeds):
    answer = []
    days = 0 #기능 완성을 위해 필요한 작업일
    count = 0 #완성된 기능 개수 카운트
    
    while len(progresses): 
        if (progresses[0]+days*speeds[0]) >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        else:
            days += 1 
            if count > 0: #몇 개의 기능이 완료된 상태에서 현재의 time으로 다음 기능의 구현 개발이 완료가 되지 않는 경우
                answer.append(count) #한 번에 배포 안되므로 카운트 끊어줌
                count = 0    
            
    answer.append(count) #else의 결과를 넣어줌
        
    return answer