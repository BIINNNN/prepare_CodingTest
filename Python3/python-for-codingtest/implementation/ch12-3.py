# 문자열 압축
def solution(s):
    answer = len(s)
    
    # 1개 단위부터 압축의 단위를 늘려가며 확인
    # 이때, 확인은 문자열의 절반길이까지 확인하면 됨. (최대 압축 단위가 문자열 절반 이상이 넘어 갈 수 없기 때문)
    for step in range(1, len(s)//2+1):
        line = ""
        count = 1
        prev = s[:step] # 앞에서부터 step(단위 크기)만큼 문자열 뽑아냄
        
        for i in range(step, len(s), step): #단위 크기만큼 증가시켜가며 이전 문자열과 같은지 비교
            if prev == s[i:i+step]:
                count += 1
            else:
                # 다른 경우 더이상 압축 불가
                line += str(count)+prev if count >= 2 else prev
                prev = s[i:i+step] #이젠 다음 문자열이 었던 i+step 구간까지의 문자열이 이전 문자열이 됨
                count = 1 # 새롭게 비교해서 카운트 해야하므로 다시 초기화
            
        # 압축되지 않고 남은 문자열이 있을 수 있으므로 이 경우에 대해 처리
        line += str(count)+prev if count >= 2 else prev
        answer = min(answer, len(line))
                
    return answer