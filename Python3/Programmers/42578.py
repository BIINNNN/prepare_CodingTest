# 위장
def solution(clothes):
    answer = 1
    closet = {}
    
    for name, kind in clothes:
        if kind in closet:
            closet[kind] += 1
        else:
            closet[kind] = 1
    print(closet)
    for key, values in closet.items():
        answer *= (values+1) # 해당 카테고리에서 안 고르는 경우까지 고려해서 (values+1) 로 계산
    
    answer -= 1 # 모든 카테고리에서 선택하지 않은 경우 제외 (아무것도 안 입는 경우)
    return answer