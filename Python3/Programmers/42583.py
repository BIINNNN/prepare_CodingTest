def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length #다리에 올라갈 수 있는 트럭의 수만큼 bridge라는 리스트 생성해서 다리 위의 상황 표시
    
    while bridge:
        answer += 1
        bridge.pop(0)
        
        if truck_weights: #대기중인 트럭 리스트 빌 때까지 반복
            if sum(bridge)+truck_weights[0] > weight:
                bridge.append(0) #두 대의 무게 합이 최대 무게보다 커진다면 한 대만 올라가도록 해야 함
            else: #최대 무대보다 작은 경우 두 대 모두 bridge에 올라갈 수 있게 됨
                bridge.append(truck_weights.pop(0))
    
    return answer