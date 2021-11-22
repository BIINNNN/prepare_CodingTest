def solution(name):
    #ord(c)는 문자의 유니코드 값을 돌려주는 함수
    name_count = [min(ord(i) - ord('A'), ord('Z') - ord(i)+1) for i in name] #최소한의 조이스틱 가동 횟수
    answer = 0
    idx = 0 #이동방향
    
    while True:
        answer += name_count[idx]
        name_count[idx] = 0
        left, right = 1, 1

        if sum(name_count) == 0:
            break
        
        #좌우 이동방향 결정
        while name_count[idx - left] == 0:
            left += 1
        while name_count[idx + right] == 0:
            right += 1
        
        #위치(idx) 조정
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer