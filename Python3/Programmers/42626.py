import heapq

def solution(scoville, K):
    heapq.heapify(scoville) #원소가 들어있는 리스트를 힙으로 변환

    cnt = 0   # 섞은 횟수

    #가장 작은 스코빌 지수가 k 이상이 될 때까지 실행
    while scoville[0] < K:
        cnt += 1

        first_scovile = heapq.heappop(scoville) #스코빌 지수가 가장 작은 음식
        second_scovile = heapq.heappop(scoville) #스코빌 지수가 두번째로 작은 음식

        mix_scovile = first_scovile + (second_scovile * 2) 

        heapq.heappush(scoville, mix_scovile) #섞은 두 음식 포함
        #음식을 모두 섞었는데도 k보다 작다면
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    
    return cnt

#어려웡..... 공부 더 해....