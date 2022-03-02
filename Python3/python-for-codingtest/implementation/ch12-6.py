def possible(answer):
    for x, y, a in answer:
        if a == 0: # 기능의 경우
            # '바닥 위' or '보의 한쪽 끝 부분 위' or '다른 기둥 위'에 있어야 함.
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False # 해당되는 경우가 없으면 불가능하므로 False 반환
        elif a == 1: # 보의 경우
            # '한쪽 끝부분이 기둥 위' or '양쪽 끝부분이 다른 보와 동시 연결' 되어 있어야 함.
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []    
    for frame in build_frame:
        x, y, a, b = frame
        if b == 0: # 삭제하는 경우
            answer.remove([x, y, a]) # 일단 먼저 삭제한 후
            if not possible(answer): # 삭제했을 때 가능한 구조인지 확인
                answer.append([x, y, a]) # 조건을 만족하지 못하면 answer에 다시 삽입(삭제 무시)
        if b == 1: # 설치하는 경우
            answer.append([x, y, a])  # 일단 설치먼저 한 후
            if not possible(answer): # 설치했을 때 가능한 구조인지 확인
                answer.remove([x, y, a])# 조건을 만족하지 못하면 answer에서 삭제(설치 무시)
    return sorted(answer) # 정렬해서 반환