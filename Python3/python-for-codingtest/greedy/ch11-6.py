#무지의 먹방 라이브 - 프로그래머스 2019 카카오 신입 공채 문제
#이 코드 실행하려면 프로그래머스에서 해당 문제 찾아서 실행해야 정상적으로 실행 가능함.
import heapq

def solution(food_times, k):
    
    # 모든 음식을 먹는데 소요되는 시간이 k보다 작으면 네트워크 장애 발생 전에 음식 다 먹게 됨
    # 따라서 장애 이후 먹을 음식 번호 없음
    if sum(food_times) <= k:
        return -1
    
    # 시간이 작은 음식부터 빼줌 - 우선순위 큐 사용
    q = [] #우선순위 큐
    for i in range(len(food_times)):
        # 우선순위 큐에 (먹는데 필요한 시간, 음식 번호) 형태로 삽입
        heapq.heappush(q, (food_times[i],i+1)) 
    
    sum_value = 0 # 음식 먹는데 지금까지 사용한 전체 시간
    previous = 0 # 바로 전 턴에 다 먹은 음식의 다 먹는데 필요한 시간
    length = len(food_times) # 남은 음식 개수 (처음엔 다 있는 상태이므로 food_times의 길이로 초기화)
    
    # 한 턴 돌면서 소요하게 되는 전체 음식 먹는 시간을 k와 비교해서 k보다 커지는 경우 턴 종료
    # 이 때, 반복문 안에서 다 먹은 음식에 대해서 우선순위 큐에서 pop 해주기 떄문에 q[0][0]을 사용
    while sum_value+((q[0][0]-previous)*length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous)*length
        length -= 1 # 남은 음식 중, 소요 시간이 짧은 음식을 다 먹었으므로 남은 음식이 하나 줄어 들게 됨.
        previous = now #지금 먹은 음식이 이제 직전에 먹은 음식이 됨.
        
    # 남은 음식들을 이제 음식 번호 기준으로 정렬
    # 장애 복구 이후 먹어야 할 음식은 시간이 아닌 회전판에서 다음 차례로 돌아오는 음식 번호 기준으로 결정하기 때문
    result = sorted(q, key = lambda x: x[1]) 
    
    return result[(k-sum_value)%length][1] #음식 번호 출력